import google.generativeai as genai

# Direct API key (⚠️ do NOT commit this to GitHub!)
genai.configure(api_key="AIzaSyB7mY6VvjecZen74hllNIVH1IAvocrDCgw")

# Define the persona and format instructions here
PERSONA_PROMPTS = {
    "Default": "You are a helpful and intelligent assistant.",
    "Expert Analyst": "You are a world-class professional analyst. Your response should be formal, data-driven, and structured. Use bullet points and **bold text** to highlight key findings.",
    "Creative Brainstormer": "You are a creative partner. Your response should be imaginative and focus on generating new ideas, possibilities, or different angles based on the document's content.",
    "ELI5 (Explain Like I'm 5)": "You are a friendly teacher explaining things to a five-year-old. Your response must be extremely simple, use easy words, and short sentences. Use analogies if possible."
}

FORMAT_PROMPTS = {
    "Default": "Please format your response clearly.",
    "Bullet Points": "Please provide your entire answer as a well-structured bulleted list.",
    "JSON": "Please provide your entire answer as a single, valid JSON object. Do not include any text or formatting outside of the JSON structure.",
    "Short Paragraph": "Please provide your answer as a single, concise paragraph."
}


def get_gemini_response(base_prompt, persona, output_format,
                        temperature=0.7, top_p=0.95, top_k=40):
    """
    Sends a request to the Gemini model with persona, format instructions, and tuning params.
    """
    model = genai.GenerativeModel(
        'gemini-1.5-flash',
        generation_config={
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
        }
    )
    
    persona_instruction = PERSONA_PROMPTS.get(persona, PERSONA_PROMPTS["Default"])
    format_instruction = FORMAT_PROMPTS.get(output_format, FORMAT_PROMPTS["Default"])
    
    final_prompt = [
        f"**Agent Instructions**\n"
        f"Persona: {persona_instruction}\n"
        f"Output Format: {format_instruction}\n\n"
        f"--------------------\n\n"
    ]
    final_prompt.extend(base_prompt)
    
    try:
        response = model.generate_content(final_prompt)
        return response.text
    except Exception as e:
        return f"Error communicating with Gemini API: {e}"


def start_chat_session(history=[], temperature=0.7, top_p=0.95, top_k=40):
    """Starts a new chat session with the Gemini model, with custom params."""
    model = genai.GenerativeModel(
        'gemini-1.5-flash-latest',
        generation_config={
            "temperature": temperature,
            "top_p": top_p,
            "top_k": top_k,
        }
    )
    chat = model.start_chat(history=history)
    return chat


def send_chat_message(chat_session, prompt):
    """Sends a message in an ongoing chat session and returns the response."""
    try:
        response = chat_session.send_message(prompt)
        return response.text
    except Exception as e:
        return f"Error sending message: {e}"
