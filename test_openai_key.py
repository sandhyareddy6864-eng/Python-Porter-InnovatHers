import openai

openai.api_key = "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"

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}],
        max_tokens=10
    )
    print("API key is working! Response:", response.choices[0].message["content"])
except Exception as e:
    print("API key error:", e)
