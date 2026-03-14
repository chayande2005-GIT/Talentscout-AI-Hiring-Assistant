from groq import Groq
from prompts import SYSTEM_PROMPT

client = Groq(api_key="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")

conversation = [{"role": "system", "content": SYSTEM_PROMPT}]

def chatbot_response(user_input):

    if len(user_input.strip()) < 2:
        return "Could you please provide more information?"
    
    if user_input.lower() in ["exit", "quit", "bye"]:
        return "Thank you for applying to TalentScout. Our team will contact you soon."

    conversation.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation
        )

        reply = response.choices[0].message.content

        conversation.append({"role": "assistant", "content": reply})

        return reply
    
    except Exception as e:
        # Remove the user message if API call fails
        conversation.pop()
        error_message = str(e)
        print(f"DEBUG - Full Error: {error_message}")  # Debug line
        
        # Return the actual error message to see what's wrong
        return f"Error: {error_message}"