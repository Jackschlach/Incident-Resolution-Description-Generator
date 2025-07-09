# Incident Resolution Description Generator

A Flask web app that transforms incident details into professional resolution descriptions using OpenAI's GPT-3.5-turbo.

## Features

1. **Clone & Install**
   ```bash
   git clone <your-repo-url>
   cd Incident-Resolution-Description-Generator
   pip install -r requirements.txt
   ```

2. **Set API Key**
   Create `.env` file:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

3. **Run**
   ```bash
   python app.py
   ```
   Visit `http://localhost:5000`

## Features

- Transform incident details into structured descriptions
- Multiple tone options (casual, professional, neutral)
- Secure API key management

## Deployment

For production (Heroku, Railway, etc.):
- Set `OPENAI_API_KEY` environment variable in your hosting platform
- Don't include `.env` file in deployment

## Security

✅ API keys stored in environment variables  
✅ `.env` file excluded from version control  
✅ Safe to share publicly on GitHub

