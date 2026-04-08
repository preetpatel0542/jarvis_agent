# jarvis_agent
# 🤖 JARVIS AI Agent — Step-by-Step Setup Guide

---

## 📋 Prerequisites

Before you begin, make sure you have:

| Requirement | Version | Download |
|-------------|---------|----------|
| Python | 3.9+ | https://python.org |
| pip | Latest | Comes with Python |
| Microphone | Any | Built-in or external |
| Internet Connection | Stable | Required for APIs |

---

## ⚙️ Step 1: Install Python

1. Go to **https://python.org/downloads**
2. Download Python **3.9 or higher**
3. During installation, check ✅ **"Add Python to PATH"**
4. Verify installation:
   ```bash
   python --version
   # Should show: Python 3.9.x or higher
   ```

---

## 📁 Step 2: Create Project Folder

```bash
# Windows
mkdir C:\Projects\Jarvis
cd C:\Projects\Jarvis

# Mac / Linux
mkdir ~/Projects/Jarvis
cd ~/Projects/Jarvis
```

Copy `jarvis.py` and `requirements.txt` into this folder.

---

## 📦 Step 3: Install Required Libraries

```bash
pip install speechrecognition
pip install pyttsx3
pip install openai==0.28.1
pip install wikipedia
pip install requests
pip install pyaudio
```

### ⚠️ PyAudio Troubleshooting

**Windows:** If PyAudio fails, run:
```bash
pip install pipwin
pipwin install pyaudio
```

**Mac:**
```bash
brew install portaudio
pip install pyaudio
```

**Linux (Ubuntu):**
```bash
sudo apt-get install python3-pyaudio portaudio19-dev
pip install pyaudio
```

---

## 🔑 Step 4: Get Your API Keys

### OpenAI API Key (for AI responses)
1. Go to **https://platform.openai.com**
2. Sign up / Log in
3. Click your profile → **View API Keys**
4. Click **"Create new secret key"**
5. Copy the key (starts with `sk-...`)

> 💡 **Free Tier:** OpenAI gives $5 free credits for new accounts

### OpenWeatherMap API Key (for weather)
1. Go to **https://openweathermap.org**
2. Sign up for a free account
3. Go to **API Keys** section
4. Your default key is ready to use

---

## ✏️ Step 5: Configure jarvis.py

Open `jarvis.py` and update these two lines:

```python
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxx"   # Your OpenAI key
WEATHER_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxx"  # Your weather key
```

Also update your name if you want:
```python
USER_NAME = "Sir"        # Change to your name
JARVIS_NAME = "Jarvis"   # Change assistant name
```

---

## ▶️ Step 6: Run JARVIS

```bash
cd C:\Projects\Jarvis    # or ~/Projects/Jarvis
python jarvis.py
```

You should hear:
> *"Good morning, Sir! I am Jarvis, your AI assistant. How can I help you today?"*

---

## 🎙️ Step 7: Try These Commands

Once JARVIS is running, try saying:

| Say This... | JARVIS Will... |
|-------------|----------------|
| `"What time is it?"` | Tell current time |
| `"What is the date?"` | Tell today's date |
| `"Open YouTube"` | Open YouTube in browser |
| `"Search for Python tutorials"` | Google search |
| `"What's the weather in Chennai?"` | Give weather update |
| `"Who is Elon Musk?"` | Wikipedia summary |
| `"Tell me a joke"` | Tell a joke 😄 |
| `"Play music"` | Open YouTube Music |
| `"What is machine learning?"` | AI explanation |
| `"Goodbye"` | Exit the program |

---

## 🐛 Common Errors & Fixes

### Error: `No module named 'speech_recognition'`
```bash
pip install speechrecognition
```

### Error: `OSError: [Errno -9996] Invalid input device`
- Check if your microphone is connected and not muted
- Try running as Administrator (Windows)

### Error: `openai.error.AuthenticationError`
- Double-check your OpenAI API key in `jarvis.py`
- Make sure there are no spaces around the key

### Error: `Could not find PyAudio`
- Follow the PyAudio Troubleshooting steps in Step 3

### Jarvis doesn't understand my voice
- Speak clearly and slowly
- Reduce background noise
- Ensure microphone is set as default input device

---

## 🚀 Level Up: Advanced Features

### Add Memory with LangChain
```bash
pip install langchain chromadb
```

### Run AI Locally (FREE — no API needed)
```bash
# Install Ollama
# Download from: https://ollama.ai
ollama pull llama2
ollama serve
```
Then change `ask_ai()` to use the local Ollama endpoint.

### Better Speech Recognition (Offline)
```bash
pip install openai-whisper
```

---

## 📂 Project File Structure

```
Jarvis/
│
├── jarvis.py              ← Main application file
├── requirements.txt       ← All dependencies
├── jarvis_notes.txt       ← Auto-created when you save notes
└── README.md              ← This guide
```

---

## 💡 Tips for Your Demo / Viva

1. **Run in a quiet room** for best voice recognition
2. **Have a backup plan** — test with text input if mic fails
3. **Show the code structure** — explain the modular design
4. **Highlight the AI integration** — this is the impressive part
5. **Prepare for "How does it work?"** — explain the voice→text→AI→voice pipeline

---

## 🆘 Need Help?

- **Python Docs:** https://docs.python.org
- **OpenAI Docs:** https://platform.openai.com/docs
- **SpeechRecognition Docs:** https://pypi.org/project/SpeechRecognition
- **pyttsx3 Docs:** https://pypi.org/project/pyttsx3

---

*Good luck with your project! 🎓🚀*
