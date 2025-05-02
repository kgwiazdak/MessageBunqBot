import json
from openai import OpenAI

def get_json_transactions_from_text(text):
    client = OpenAI(
    base_url = 'https://integrate.api.nvidia.com/v1',
    api_key = "XYZ"
  )

    messages=[{"role":"user","content":f''' You are a Creative Storyteller. When I give you a list of bank transactions, you will:

1. Split the transactions into groups of up to 3 (if there are 5 transactions, you’ll produce 2 stories: one with 3 items and one with 2).
2. For each group, write a short, humorous narrative using those transactions as plot points (date, amount, merchant).
3. Vary the style every time (e.g., film noir, fairytale, sitcom script, sci‑fi adventure, pirate saga, mock‑epic poem).
4. Invent fresh characters for each story.
5. Keep it concise (around 200–300 words per story).
6. Return **only** a JSON array of objects, each with a single `story` field:
these are the transactions:
{text}'''}]
    completion = client.chat.completions.create(
    model="mistralai/mistral-7b-instruct-v0.3",
    messages=messages,
  )
    return completion.choices[0].message.content


json_transaction = json.loads(get_json_transactions_from_text("""
Amount: 250 EUR, Description: Online shopping (12/12/21)
Amount: 100 EUR, Description: Groceries (10/12/21)
Amount: 20 EUR, Description: Coffee shop (08/12/21)
Amount: 500 EUR, Description: Rent payment (05/12/21)
Amount: 30 EUR, Description: Utility bills (01/12/21)
                                      """))

for transaction in json_transaction:
    print(transaction['story'])