import openai
import os

# Set your OpenAI API key securely
openai.api_key = os.getenv ("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")  # Recommended way

# OR hardcode if you're just testing (not safe for production):
# openai.api_key = "sk-..."  # ⚠️ Not recommended in real projects

def generate_resolution_description(paragraph):
    prompt = (
        "You are an assistant that turns incident paragraphs into professional resolution descriptions.\n"
        "Format it like this:\n"
        "Due to (root cause), users experienced (the issue). This was resolved by (resolving team) doing (resolution).\n\n"
        f"Paragraph: {paragraph}\n"
        "Resolution Description:"
    )

    response = openai.chat.completions.create(
        model="gpt-4-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
        max_tokens=150
    )

    return response.choices[0].message.content.strip()


# TEST THE FUNCTION
if __name__ == "__main__":
    input_paragraph = input("Paste your incident paragraph: ")
    result = generate_resolution_description(input_paragraph)
    print("\nGenerated Resolution Description:\n")
    print(result)



