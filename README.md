# Incident Resolution Description Generator

A Flask web app that transforms incident details into professional resolution descriptions using OpenAI's GPT-3.5-turbo.

## Quickstart
1. Clone the repo & install dependencies:
   ```bash
   git clone <your-repo-url>
   cd Incident-Resolution-Description-Generator
   pip install -r requirements.txt
   ```
2. Add your OpenAI API key to a `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
3. Run the app:
   ```bash
   python app.py
   ```
   Visit [http://localhost:5001](http://localhost:5001)

## Features
- Instantly generate incident resolution summaries
- Switch between professional, casual, and neutral tones
- Clean, responsive web UI

## Built With
- Python, Flask
- OpenAI API (GPT-3.5-turbo)
- HTML, CSS, JavaScript

---
API keys are kept secure in environment variables. Do not commit your `.env` file.

