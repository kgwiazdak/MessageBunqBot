import os
import base64
from openai import OpenAI, Client
import json

api_key = os.getenv("OPENAPIKEY") or input("Enter your OpenAI API key: ")
client = Client(api_key=api_key)

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def call_gpt_image2text(client, image_path):
    base64_image = encode_image_to_base64(image_path)
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Get text from the image. Dont write anything else."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                            "detail": "high"
                        }
                    }
                ]
            }
        ],
        max_tokens=300,
    )
    return response.choices[0].message.content

def get_json_transactions_from_text(text):
    client = OpenAI(
    base_url = 'https://integrate.api.nvidia.com/v1',
    api_key = "XYZ"
  )


    messages=[{"role":"user","content":f"Your job is to extract transactions from this text like and return it as a json in form product: price Your response is just json, dont write any aditional comments {text}"}]
    completion = client.chat.completions.create(
    model="mistralai/mistral-7b-instruct-v0.3",
    messages=messages,
  )
    return completion.choices[0].message.content

def run_receips_pipeline(image_path):
    text = call_gpt_image2text(client, image_path)
    json_transactions = get_json_transactions_from_text(text)
    json_transactions = json.loads(json_transactions)
    return json_transactions



