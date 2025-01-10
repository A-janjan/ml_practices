from groq import Groq

api_key = 'groq_api_key'

client = Groq(
    api_key=api_key,
)


import pandas as pd
import numpy as np


system_message = """
You are a binary classifier for sentiment analysis.
Given a text, based on its sentiment, you classify it into one of two
categories: positive or negative.
You can use the following texts as examples:
Text: "I love this product! It's fantastic and works perfectly."
Positive
Text: "I'm really disappointed with the quality of the food."
Negative
Text: "This is the best day of my life!"
Positive
Text: "I can't stand the noise in this restaurant."
Negative
ONLY return the sentiment as output (without punctuation).
Text:
"""

df = pd.read_csv('movie.csv', encoding='utf-8')
df['label'] = df["label"].replace({0: 'Negative', 1:'Positive'})

def process_text(text):
    response = client.chat.completions.create(
        messages=[
            {"role": "system","content": system_message},
            {"role": "user", "content": text},
        ],
        model="llama3-8b-8192",
    )

    return response.choices[0].message.content


df['predicted'] = df['text'].apply(process_text)

print(df)