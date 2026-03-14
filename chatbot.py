import openai
from prompts import SYSTEM_PROMPT

openai.api_key = "YOUR_API_KEY"

conversation = [{"role": "system", "content": SYSTEM_PROMPT}]

def chatbot_response(user_input):

    if len(user_input.strip()) < 2:
        return "Could you please provide more information?"
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        return "Thank you for applying to TalentScout. Our team will contact you soon."

    conversation.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation
    )

    reply = response.choices[0].message.content

    conversation.append({"role": "assistant", "content": reply})

    return reply