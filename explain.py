from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(" OPENAI_API_KEY not found! Make sure .env is correct.")

client = OpenAI(api_key=api_key)

def get_explanation(object_name, level="child"):
    prompt = f"""You are a super friendly AI tutor. Explain '{object_name}' to a {level}-level learner.

Include:
- Use / Purpose
- Real-world examples
- Where it’s found / seen
- Fun facts or trivia
- Safety notes (if needed)
- Compare with similar things
- "Why?" chains
- Analogy
- Suggest optional animations or stories

Be warm and spark curiosity."""

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",  
    messages=[{"role": "user", "content": prompt}],
    temperature=0.7
)

    return response.choices[0].message.content

