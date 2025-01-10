from groq import Groq

api_key = 'groq_api_key'

client = Groq(
    api_key=api_key,
)


system_message = """
You are a Python expert who produces Python code as per the user's request.
===>START EXAMPLE
---User Query---
Give me a function to print a string of text.
---User Output---
Below you can find the described function:
```def my_print(text):
return print(text)
```
<===END EXAMPLE
"""
query = "generate a Python function to calculate the nth Fibonacci number"


chat_completion = client.chat.completions.create(
    messages=[
        {"role": "user","content": system_message},
        {"role": "user", "content": query},
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)