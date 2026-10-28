import os

SYSTEM_PROMPT = "You are a helpful AI Health Assistant tailored for Pakistan's air quality health risks. Provide immediate, AI-driven medical guidance on masks, safe limits, and symptoms."

def call_groq(messages):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        return "Groq API key not found. Please set the GROQ_API_KEY environment variable."
    
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            messages=messages,
            model="llama3-70b-8192",
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling Groq API: {str(e)}"
