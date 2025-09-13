import openai

# 🔑 Replace with your OpenAI API Key
openai.api_key = "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"
try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}],
        max_tokens=10
    )
    print("API key is working! Response:", response.choices[0].message["content"])
except Exception as e:
    print("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:", e)

def rule_based_reply(query: str) -> str:
    q = query.lower()
    if "kamaya" in q or "earning" in q:
        return "Aaj aapne 1200 rupaye kharche kaat ke kamaye. 🚚"
    elif "penalty" in q:
        return "Penalty isliye lagi kyunki delivery 30 minute late hui thi."
    elif "business" in q or "behtar" in q:
        return "Aapka vyapar pichle hafte se 15% behtar hai. 👍"
    elif "help" in q or "sahayata" in q:
        return "Emergency ke liye 1 dabaiye, aur turant call connect hoga."
    else:
        return "Maaf kijiye, main aapka prashn samajh nahi paaya. Kripya phir se koshish kijiye."

def ask_ai(query: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Porter Saathi, a helpful, voice-first AI assistant for drivers with limited literacy. Respond in simple Hindi (or Hinglish if needed) with short, clear sentences."},
                {"role": "user", "content": query},
            ],
            max_tokens=200,
            temperature=0.1,
        )
        return response.choices[0].message["content"].strip()
    except Exception:
        # 🔁 Fallback if OpenAI fails
        return rule_based_reply(query)
