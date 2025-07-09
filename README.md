# Incident Resolution Description Generator

A Flask web application that transforms incident details into professional resolution descriptions using OpenAI's GPT-3.5-turbo model.

## Features

- Transform incident details into structured resolution descriptions
- Multiple tone options: casual, professional, and neutral
- Clean, modern web interface
- Secure API key management

## Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repository-url>
cd Incident-Resolution-Description-Generator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up environment variables
Create a `.env` file in the project root with your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

**Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

### 4. Run the application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Deployment

### Local Development
- The `.env` file is used for local development
- API keys are loaded from environment variables

### Production Deployment
For production deployment (Heroku, Railway, etc.):

1. Set the environment variable `OPENAI_API_KEY` in your hosting platform
2. Remove or don't include the `.env` file in your deployment
3. The application will automatically use the environment variable from the hosting platform

### GitHub Deployment
The code is now secure for GitHub deployment because:
- API keys are not hardcoded in the source code
- `.env` file is in `.gitignore` and won't be committed
- Environment variables are used for configuration

## Security Notes

- ✅ API keys are stored in environment variables, not in code
- ✅ `.env` file is excluded from version control
- ✅ No sensitive data in the repository
- ✅ Safe to share code publicly

## Usage

1. Enter incident details in the text area
2. Select your preferred tone (casual, professional, or neutral)
3. Click "Generate Description"
4. Get a professionally formatted incident resolution description

## File Structure

```
Incident-Resolution-Description-Generator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (not in git)
├── .gitignore           # Git ignore rules
├── templates/
│   └── index.html       # Web interface
├── static/
│   └── styles.css       # Styling
└── README.md            # This file
```

