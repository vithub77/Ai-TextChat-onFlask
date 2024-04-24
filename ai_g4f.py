# pip install -U g4f[all]
# ip install curl_cffi
import g4f.models
from g4f.client import Client


async def ai_response(text: str):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        # model=g4f.models.gpt_4,
        messages=[{"role": "user", "content": f"{text}"}])
    return response.choices[0].message.content
