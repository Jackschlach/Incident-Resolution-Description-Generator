import os
from flask import Flask, render_template, request
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with your API key from environment variable
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Initialize the Flask app


app = Flask(__name__)

def process_input(user_input, tone):
    """
    Transforms the user input into an incident resolution description format:
    "Due to an issue with (root cause or issue), users experienced (whatever the frontend impact was/or whatever happened). This was resolved by (team doing whatever the fix was)."
    """
    prompt = (
        f"Transform the following into an incident resolution description: "
        f"'{user_input}'\n\n"
        "The output should be in a professional, smart, informational tone and in this format:\n"
        "Due to an issue with (root cause), users experienced (issue). This was resolved by (team)."
    )

    if tone == "casual":
        prompt += " Use a casual, conversational tone."
    elif tone == "professional":
        prompt += " Use a professional and smart tone."
    else:  # default to neutral
        prompt += " Use a clear, straight to the point tone. Limit the amount of words and follow this format exactly: Due to an issue with (root cause), users experienced (issue). This was resolved by (team) doing (resolution)."

    try:
        # Use the Chat Completions API to generate the response
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Transform the incident details into a resolution description."},
                {"role": "user", "content": prompt}
            ]
        )

        # Extract and return the output text
        content = response.choices[0].message.content
        return content.strip() if content else "No response generated"

    except Exception as e:
        return f"Error generating response: {e}"

# Define the route for the home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["user_input"]
        tone = request.form.get("tone", "neutral")  # Default tone is neutral
        resolution = process_input(user_input, tone)
        return render_template("index.html", resolution=resolution, user_input=user_input, selected_tone=tone)

    return render_template("index.html", resolution=None)

if __name__ == "__main__":
    app.run(debug=True)


