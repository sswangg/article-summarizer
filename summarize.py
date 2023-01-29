import os
import openai
from dotenv import load_dotenv


load_dotenv()
openai.api_key = os.getenv("api-token")


def get_article_summary(content):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=generate_prompt(content),
        temperature=0.6,
        max_tokens=3000,
    )
    return response.choices[0].text


def generate_prompt(content):
    return f"""Summarize the article in 3-5 sentences:

Article: {content}

Summary:"""
