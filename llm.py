# llm.py

from groq import Groq

client = Groq(api_key="USE YOUR API KEY HERE")

MODEL = "llama-3.1-8b-instant"


def generate_response(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {"role": "system", "content": "Return short, clean, strict JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"Error: {str(e)}"