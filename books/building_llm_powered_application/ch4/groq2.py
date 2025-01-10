from groq import Groq

api_key = 'groq_api_key'

client = Groq(
    api_key=api_key,
)


system_message = """
You are an AI assistant specialized in solving riddles.
Given a riddle, solve it the best you can.
Provide a clear justification of your answer and the reasoning behind it.
Riddle:
"""


riddle = """
What has a face and two hands, but no arms or legs?
"""

chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user","content": system_message},
        {"role": "user", "content": riddle},
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)