# Generate many outputs, then use the model to pick the best one

from groq import Groq

api_key = 'groq_api_key'

client = Groq(
    api_key=api_key,
)


system_message = """
You are an AI assistant specialized in solving riddles.
Given a riddle, you have to generate three answers to the riddle.
For each answer, be specific about the reasoning you made.
Then, among the three answers, select the one that is most plausible given the
riddle.

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