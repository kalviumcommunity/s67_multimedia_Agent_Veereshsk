from modules.gemini_utils import start_chat_session, send_chat_message

def run_gemini():
    chat = start_chat_session()
    print("Gemini Chat Started (type 'exit' to quit)\n")

    # Default persona/format memory
    persona_choice = "Default"
    format_choice = "Default"
    custom_instr = None

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chat ended.")
            break

        # Allow runtime changes
        change_mode = input("Change persona/format? (y/n): ").strip().lower()
        if change_mode == "y":
            persona_choice = input("Persona (Default/Expert Analyst/Creative Brainstormer/ELI5): ") or persona_choice
            format_choice = input("Format (Default/Bullet Points/JSON/Short Paragraph): ") or format_choice
            custom_instr = input("Custom Instructions (optional): ") or custom_instr

        response = send_chat_message(chat, user_input, persona=persona_choice,
                                     output_format=format_choice, custom_instructions=custom_instr)
        print(f"Gemini: {response}\n")


if __name__ == "__main__":
    run_gemini()
