from groq import Groq

api_key = 'groq_api_key'

client = Groq(
    api_key=api_key,
)




system_message = """
You are an AI marketing assistant. You help users to create taglines for new
product names.
Given a product name, produce a tagline similar to the following examples:
Peak Pursuit - Conquer Heights with Comfort
Summit Steps - Your Partner for Every Ascent
Crag Conquerors - Step Up, Stand Tall
Product name:
"""


product_name = 'Elevation Embrace'


chat_completion = client.chat.completions.create(
    messages=[
        {"role": "system","content": system_message},
        {"role": "user", "content": product_name},
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)