from groq import Groq

api_key = 'groq_api_key'

client = Groq(
    api_key=api_key,
)


system_message = """
You are an AI assistant that helps humans by generating tutorials given a
text.
You will be provided with a text. If the text contains any kind of
istructions on how to proceed with something, generate a tutorial in a
bullet list.
Otherwise, inform the user that the text does not contain any
instructions.
Text:
"""

instructions = """
To prepare the known sauce from Genova, Italy, you can start by toasting
the pine nuts to then coarsely
chop them in a kitchen mortar together with basil and garlic. Then, add
half of the oil in the kitchen mortar and season with salt and pepper.
Finally, transfer the pesto to a bowl and stir in the grated Parmesan
cheese.
"""

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user","content": system_message},
        {"role": "user", "content": instructions},
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)