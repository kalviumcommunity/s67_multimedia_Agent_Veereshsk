from modules.gemini_utils import get_gemini_response

if __name__ == "__main__":
    prompt = ["Explain quantum computing in simple terms."]
    response = get_gemini_response(
        base_prompt=prompt,
        persona="Expert Analyst",
        output_format="Bullet Points",
        temperature=0.9,
        top_p=0.8,
        top_k=50
    )
    print(response)
