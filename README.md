# TalentScout AI Hiring Assistant 🤖

An intelligent AI-powered chatbot for automated candidate screening and technical assessment. The assistant collects candidate information, asks tailored technical questions based on their tech stack, and maintains a professional conversation throughout the interview process.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-v1.0+-red)
![Groq API](https://img.shields.io/badge/Groq-API-orange)

---

## 📋 Features

- ✅ **Automated Candidate Screening** - Collects essential candidate information systematically
- ✅ **Intelligent Question Generation** - Generates technical questions based on candidate's tech stack
- ✅ **Context-Aware Conversations** - Maintains conversation history for natural dialogue flow
- ✅ **Serial Question Asking** - Asks one question at a time for better user experience
- ✅ **Professional UI** - Built with Streamlit for a modern, user-friendly interface
- ✅ **Exit Handling** - Graceful conversation termination with polite goodbye messages
- ✅ **Error Handling** - Robust error management and user-friendly error messages
- ✅ **Input Validation** - Validates user input with minimum character requirement

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.14+** | Core programming language |
| **Streamlit** | Web UI framework |
| **Groq API** | LLM (Large Language Model) backend |
| **python-dotenv** | Environment variable management |
| **LLaMA 3.1** | AI model for intelligent responses |

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Groq API key (get it free from [console.groq.com](https://console.groq.com))
- Git

### Step 1: Clone the Repository
```bash
git clone https://github.com/chayande2005-GIT/Talentscout-AI-Hiring-Assistant.git
cd Talentscout-AI-Hiring-Assistant
```

### Step 2: Create Virtual Environment
```bash
python -m venv .venv

# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
Create a `.env` file in the project root:
```bash
cp .env.example .env
```

Edit `.env` and add your Groq API key:
```
GROQ_API_KEY=gsk_your_api_key_here
```

Get your free API key from [Groq Console](https://console.groq.com).

---

## 🚀 Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Interact with the Chatbot
1. Type your message in the input field
2. The chatbot will ask information one question at a time
3. Type `exit`, `quit`, or `bye` to end the conversation

---

## 📁 Project Structure

```
Talentscout-AI-Hiring-Assistant/
├── app.py                 # Streamlit main application
├── chatbot.py            # Chatbot logic and API integration
├── prompts.py            # System prompt for LLM
├── requirements.txt      # Python dependencies
├── .env.example         # Example environment variables
├── .gitignore           # Git ignore rules
├── data/
│   └── candidates.json  # Candidate data storage
└── README.md            # This file
```

---

## 🔧 How It Works

### Architecture Overview

```
User Input (Streamlit UI)
        ↓
    app.py (Display & Session Management)
        ↓
    chatbot.py (Process & API Call)
        ↓
    Groq API (LLaMA 3.1 Model)
        ↓
    AI Response
        ↓
    Display in Chat UI
```

### Key Components

**1. app.py** - Streamlit Interface
- Page configuration with emoji icon 🤖
- Chat message display
- Session state management for conversation history
- Sidebar with project information

**2. chatbot.py** - Core Logic
- Groq API integration
- Input validation (minimum 2 characters)
- Exit detection (exit, quit, bye)
- Error handling with user-friendly messages
- Conversation history management

**3. prompts.py** - System Prompt
- Defines chatbot personality and behavior
- Instructs the AI to ask questions serially (one at a time)
- Collection sequence: Name → Email → Phone → Experience → Position → Location → Tech Stack
- Technical question generation based on tech stack

---

## 💬 Information Collected

The chatbot collects the following candidate information:

1. **Full Name** - Candidate's complete name
2. **Email** - Contact email address
3. **Phone Number** - Contact phone number
4. **Years of Experience** - Professional experience level
5. **Desired Position** - Position they're applying for
6. **Location** - Current/preferred location
7. **Tech Stack** - Technologies they work with
8. **Technical Questions** - 3-5 questions based on their tech stack

---

## 🔑 API Setup

### Getting Groq API Key

1. Visit [Groq Console](https://console.groq.com)
2. Sign up (free account)
3. Navigate to **API Keys**
4. Click **Create New API Key**
5. Copy the key and paste in your `.env` file

### Why Groq?
- ✅ Free tier with generous limits
- ✅ Fast inference (30+ tokens/second)
- ✅ No credit card required
- ✅ Unlimited API calls on free plan
- ✅ Multiple LLM models available

---

## 🎯 Example Conversation

```
You: Hi
Bot: Hello! Welcome to TalentScout. I'm here to help screen your application for a technical position. Let's start with the basics. What is your full name?

You: John Smith
Bot: Nice to meet you, John! Thank you for providing that. Now, what is your email address?

You: john@example.com
Bot: Got it! For further communication, could you please share your phone number?

You: 555-123-4567
Bot: Thank you! How many years of professional experience do you have?

... and so on
```

---

## ⚠️ Security

- **Never commit your `.env` file** - It contains sensitive API keys
- `.env` is listed in `.gitignore` to prevent accidental commits
- Use `.env.example` as a template for setting up locally
- Rotate API keys periodically for enhanced security

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 Improvements & Future Enhancements

- [ ] Support for multiple languages
- [ ] Interview recording/transcription
- [ ] Candidate scoring system
- [ ] Integration with ATS (Applicant Tracking Systems)
- [ ] Advanced NLP for better question generation
- [ ] Email sending for follow-ups
- [ ] Data export to CSV/PDF
- [ ] Multi-user support

---

## 🐛 Troubleshooting

### Issue: "GROQ_API_KEY environment variable not set"
**Solution:** Create a `.env` file with your API key:
```
GROQ_API_KEY=gsk_your_key_here
```

### Issue: "Module not found: groq"
**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: Chatbot not responding
**Solution:** Check that:
1. Your `.env` file contains a valid Groq API key
2. Internet connection is active
3. Groq API is not experiencing outages

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**TalentScout Team**

---

## 📞 Support

For issues, questions, or suggestions, please open an [Issue](https://github.com/chayande2005-GIT/Talentscout-AI-Hiring-Assistant/issues).

---

## 🌟 Acknowledgments

- [Groq](https://groq.com) - For providing fast, free LLM API
- [Streamlit](https://streamlit.io) - For making web app development easy
- [LLaMA](https://llama.meta.com) - For the LLM model
