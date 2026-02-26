from groq import Groq

client = Groq(api_key="abcdefghijklmnopqrstuvwxyz")
def build_prompt(topic, mode):
    if mode == "shakespeare":
        return f"""
        Thou art a wise scholar.
        Explain the topic "{topic}" in the style of William Shakespeare.
        Use poetic English, old words, and dramatic tone.
        Keep it clear but artistic.
        """

    elif mode == "pirate":
        return f"""
        Ye be a pirate teacher of the high seas.
        Explain "{topic}" like a pirate.
        Use pirate slang, sea metaphors, and fun tone.
        """

    elif mode == "bandit":
        return f"""
        You are a rough street-smart bandit.
        Explain "{topic}" in a bold, casual, desi-street style.
        Keep it simple, confident, and slightly dramatic.
        """

    else:
        return f"Explain {topic} simply."
def explain_topic(topic, mode):
    prompt = build_prompt(topic, mode)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.8
    )

    return response.choices[0].message.content
topic = input("Enter topic: ")
mode = input("Choose mode (shakespeare/pirate/bandit): ")


output = explain_topic(topic, mode)
print("\n--- AI Explanation ---\n")
print(output)
