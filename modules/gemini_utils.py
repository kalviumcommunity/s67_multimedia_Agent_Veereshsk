import google.generativeai as genai
# ⚠️ Load API key from env var in production (not hardcoded)
genai.configure(api_key="API_KEY_HERE")

PERSONA_PROMPTS = {
    "Default": "You are a helpful and intelligent assistant.",
    "Expert Analyst": "You are a world-class professional analyst. Formal, data-driven, structured. Use bullet points and **bold text** to highlight findings.",
    "Creative Brainstormer": "You are a creative partner. Be imaginative and generate new ideas or perspectives.",
    "ELI5": "You are a friendly teacher explaining things to a five-year-old. Use extremely simple words and short sentences."
}

FORMAT_PROMPTS = {
    "Default": "Please format your response clearly.",
    "Bullet Points": "Provide your entire answer as a well-structured bulleted list.",
    "JSON": "Provide your entire answer as a single, valid JSON object. No text outside the JSON.",
    "Short Paragraph": "Provide your answer as a single, concise paragraph."
}


def build_dynamic_prompt(base_prompt, persona="Default", output_format="Default", custom_instructions=None):
    """
    Builds a dynamic prompt merging persona, format, and custom instructions.
    """
    persona_instruction = PERSONA_PROMPTS.get(persona, PERSONA_PROMPTS["Default"])
    format_instruction = FORMAT_PROMPTS.get(output_format, FORMAT_PROMPTS["Default"])
    custom_instruction_text = f"\nCustom Instructions: {custom_instructions}\n" if custom_instructions else ""

    return (
        f"**Agent Instructions**\n"
        f"Persona: {persona_instruction}\n"
        f"Output Format: {format_instruction}\n"
        f"{custom_instruction_text}\n"
        f"--------------------\n\n"
        f"{base_prompt}"
    )


def get_gemini_response(base_prompt, persona="Default", output_format="Default",
                        custom_instructions=None, temperature=0.7, top_p=0.95, top_k=40):
    """
    One-shot request (no chat memory).
    """
    model = genai.GenerativeModel(
        'gemini-1.5-flash',
        generation_config={"temperature": temperature, "top_p": top_p, "top_k": top_k}
    )

    final_prompt = build_dynamic_prompt(base_prompt, persona, output_format, custom_instructions)

    try:
        response = model.generate_content(final_prompt)
        return response.text
    except Exception as e:
        return f"Error communicating with Gemini API: {e}"


def start_chat_session(history=None, temperature=0.7, top_p=0.95, top_k=40):
    """
    Starts a new chat session with Gemini.
    """
    if history is None:
        history = []
    model = genai.GenerativeModel(
        'gemini-1.5-flash-latest',
        generation_config={"temperature": temperature, "top_p": top_p, "top_k": top_k}
    )
    return model.start_chat(history=history)


def send_chat_message(chat_session, prompt, persona="Default", output_format="Default", custom_instructions=None):
    """
    Sends a dynamically formatted message inside an ongoing chat.
    """
    final_prompt = build_dynamic_prompt(prompt, persona, output_format, custom_instructions)
    try:
        response = chat_session.send_message(final_prompt)
        return response.text
    except Exception as e:
        return f"Error sending message: {e}"
