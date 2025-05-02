import requests
import json
import discord
from discord import app_commands
from discord.ext import commands
from openai import OpenAI
from receips import run_receips_pipeline
from debt import *

import api_keys
from api_tools import tools
from bunq_functions import get_last_transactions, pay
import os
import uuid


SESSION_USER_ID = str(uuid.uuid4())


client = OpenAI(
  base_url='https://integrate.api.nvidia.com/v1',
  api_key=api_keys.deepseek_r1
)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

transactions = Transactions()
users = Users()


def generate_reply(user_msg):
    prompt = f"""
    You are a smart and helpful financial assistant connected to the user's bank account.
    This is the user prompt to answer: "{user_msg}".
    """
    messages = [{"role": "user", "content": prompt}]
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
        tools=tools,
        user=SESSION_USER_ID
    )

    try:
        tool_call = completion.choices[0].message.tool_calls[0]
        function_name = tool_call.function.name
        arguments = json.loads(tool_call.function.arguments)

        messages.append({
            "role": "assistant",
            "content": None,
            "tool_calls": [tool_call.model_dump()]
        })

        if function_name == "get_last_transactions":
            result = get_last_transactions(**arguments)
        elif function_name == 'pay':
            result = pay(**arguments)
        elif function_name == 'request_payment':
            result = request_payment(**arguments)
        elif function_name == "generate_image":
            result = generate_image(**arguments)

        print(tool_call)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": result
        })

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
            tools=tools,
            user=SESSION_USER_ID
        )
        print(completion.choices[0].message.content)
    except TypeError as e:
        print('No function call detected', e)

    return completion.choices[0].message.content


def generate_image(prompt: str):
    response = client.images.generate(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024",
        quality="standard"
    )
    image_url = response.data[0].url
    return f"🖼️ **Image for prompt:** *{prompt}*\n\n![Generated Image]({image_url})"


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.tree.sync() 
    print("Slash commands have been registered.")


@bot.tree.command(name="bunq", description="Send prompt to bunq assistant")
@app_commands.describe(prompt="Promp to Bunkewsky",
                       image="Optional image to accompany your prompt")
async def transactions_command(interaction: discord.Interaction,
                               prompt: str, image: discord.Attachment = None):
    await interaction.response.defer(thinking=True)

    try:
        if image:

            curr_transactions = run_receips_pipeline(image.url)
            for key, value in curr_transactions.items():
                transactions.add_transaction(Transaction(
                    user_number=None,
                    name=key,
                    amount=float(value[1:]),
                    currency=value[0:1]
                ))

            transactions_list = transactions.get_all_transactions_with_no_user()
            transactions = "\n".join([f"{t.name}: {t.amount}" for t in transactions_list])
            await interaction.followup.send(f"Current transactions without user: \n{transactions}")


        reply = generate_reply(prompt)
        await interaction.followup.send(reply)
    except Exception as e:
        await interaction.followup.send("An error occurred while processing the prompt.")
        print("Error:", e)


bot.run(api_keys.discord_token)
