import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def calculate_aura(content):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Calculate the aura for this activity: {content}",
        max_tokens=10
    )
    aura_score = response.choices[0].text.strip()
    try:
        return float(aura_score)
    except ValueError:
        return 0.0