"""
JARVIS AI AGENT - College Project
Author: [patel preet]
Description: A voice-activated AI assistant built with Python
"""
#  cd C:\Users\HP\Desktop\google` ai\jarvis-ui
#  npm run dev -- --port 5173
import sqlite3
import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import requests
import json
import time
import random

# ─────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────
GEMINI_API_KEY = "AIzaSrgyCihhnYExvUyfhVa_AGbd7Ti_VfhWKxTv541Ns"   # Google Gemini
WEATHER_API_KEY = "4bab14a309dtd412585fbadfut50a870bbd63c"  # Get from openweathermap.org
JARVIS_NAME = "Jarvis"
USER_NAME = "preet patel"

# ─────────────────────────────────────────
#  VOICE ENGINE SETUP
# ─────────────────────────────────────────
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 = Male, 1 = Female
engine.setProperty('rate', 175)             # Speech speed
engine.setProperty('volume', 1.0)          # Volume: 0.0 to 1.0


def speak(text: str):
    """Convert text to speech."""
    print(f"\n{JARVIS_NAME}: {text}")
    engine.say(text)
    engine.runAndWait()


def listen() -> str:
    """Listen for voice command and return as text."""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("\n[Listening...]")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                query = recognizer.recognize_google(audio, language='en-in')
                print(f"You: {query}")
                return query.lower()
            except sr.WaitTimeoutError:
                return ""
            except sr.UnknownValueError:
                speak("Sorry, I didn't catch that. Please repeat.")
                return ""
            except sr.RequestError:
                speak("Speech recognition service is unavailable.")
                return ""
    except Exception as e:
        print(f"[ERROR] Microphone error: {e}")
        print("[INFO] Using text input mode. Type your command:")
        try:
            return input("You: ").lower()
        except:
            return ""


# ─────────────────────────────────────────
#  AI BRAIN - GOOGLE GEMINI API
# ─────────────────────────────────────────
def ask_ai(prompt: str) -> str:
    """Send prompt to Google Gemini and return response."""
    try:
        url = (
            f"https://generativelanguage.googleapis.com/v1beta/models/"
            f"gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
        )
        headers = {"Content-Type": "application/json"}
        system_note = (
            f"You are {JARVIS_NAME}, a helpful AI assistant like Iron Man's JARVIS. "
            f"Be concise and reply in 2-3 sentences max. "
            f"You can understand and answer in English, Hindi, and Gujarati. "
            f"Always reply in the same language as the user's prompt or the language they request. "
            f"IMPORTANT: If you respond in Hindi or Gujarati, you MUST write your response using the English/Latin alphabet (like Hinglish or Gujlish) so the default text-to-speech engine can pronounce it correctly."
        )
        data = {
            "contents": [
                {"parts": [{"text": system_note + "\n\nUser: " + prompt}]}
            ]
        }
        response = requests.post(url, headers=headers, json=data, timeout=10)
        result = response.json()

        # Show debug info if error
        if "candidates" not in result:
            err_msg = result.get("error", {}).get("message", str(result))
            print(f"\n[DEBUG] Gemini Error: {err_msg}")
            return f"Gemini Error: {err_msg}"

        return result["candidates"][0]["content"]["parts"][0]["text"].strip()
    except Exception as e:
        print(f"\n[DEBUG] Exception: {e}")
        return f"Sorry {USER_NAME}, connection failed: {str(e)}"


# ─────────────────────────────────────────
#  FEATURE MODULES
# ─────────────────────────────────────────

def get_greeting() -> str:
    """Return time-based greeting."""
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    return "Good night"


def tell_time():
    """Speak current time."""
    now = datetime.datetime.now()
    speak(f"The current time is {now.strftime('%I:%M %p')}, {USER_NAME}.")


def tell_date():
    """Speak current date."""
    now = datetime.datetime.now()
    speak(f"Today is {now.strftime('%A, %B %d, %Y')}.")


def search_wikipedia(topic: str):
    """Search Wikipedia and speak a clean, concise summary."""
    try:
        import wikipedia
        topic = topic.strip()
        speak(f"Searching Wikipedia for {topic}...")
        summary = wikipedia.summary(topic, sentences=2)
        result = summary[:300]  # Limit response for clean UI & TTS
        speak(result)
    except wikipedia.exceptions.DisambiguationError as e:
        options = ", ".join(e.options[:3])
        speak(f"Too many results for {topic}. Did you mean: {options}? Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak(f"Sorry, I couldn't find a Wikipedia page for {topic}.")
    except Exception:
        speak(f"Sorry, I couldn't retrieve information about {topic} right now.")


def open_website(site: str):
    """Open a website in the browser."""
    sites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "gmail": "https://gmail.com",
        "github": "https://github.com",
        "ai": "https://openai.com",
        "stackoverflow": "https://stackoverflow.com",
    }
    url = sites.get(site, f"https://www.google.com/search?q={site}")
    webbrowser.open(url)
    speak(f"Opening {site} for you, {USER_NAME}.")


def get_weather(city: str = "Chennai"):
    """Fetch and speak current weather."""
    try:
        url = (
            f"http://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
        )
        data = requests.get(url, timeout=5).json()
        if data.get("cod") == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            speak(
                f"Weather in {city}: {desc}, "
                f"{temp:.1f} degrees Celsius, humidity {humidity} percent."
            )
        else:
            speak("Couldn't fetch weather data right now.")
    except Exception:
        speak("Weather service is unavailable.")


def tell_joke():
    """Tell a random programming joke."""
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
        "Why did the AI break up with the internet? Too many connections!",
        "A SQL query walks into a bar and asks two tables: Can I join you?",
        "Why do Java developers wear glasses? Because they don't see sharp!",
    ]
    speak(random.choice(jokes))


def take_note(note: str):
    """Save a quick note to file."""
    with open("jarvis_notes.txt", "a") as f:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"[{timestamp}] {note}\n")
    speak(f"Note saved: {note}")


# ─────────────────────────────────────────
#  CHAT HISTORY  (text file)
# ─────────────────────────────────────────

def save_chat(user_input: str, bot_response: str):
    """Append a timestamped conversation turn to today's chat log file."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # One file per day: e.g. chat_2026-04-04.txt
    filename = "chat_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".txt"
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}]\n")
        f.write(f"User   : {user_input}\n")
        f.write(f"Jarvis : {bot_response}\n")
        f.write("-" * 50 + "\n")


def clear_chat():
    """Wipe today's chat log file."""
    filename = "chat_" + datetime.datetime.now().strftime("%Y-%m-%d") + ".txt"
    open(filename, "w").close()
    speak("Chat history cleared.")


# ─────────────────────────────────────────
#  DATABASE  (SQLite – chat.db)
# ─────────────────────────────────────────

DB_FILE = "chat.db"


def init_db():
    """Create the chats table if it doesn't exist yet."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chats (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            user      TEXT,
            bot       TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()
    print("[DB] Database initialised → chat.db")


def save_chat_db(user: str, bot: str):
    """Insert one conversation turn into the database."""
    if not (user.strip() and bot.strip()):
        return
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chats (user, bot) VALUES (?, ?)",
        (user, bot)
    )
    conn.commit()
    conn.close()


def get_all_chats(limit: int = 0):
    """Return all (or the last *limit*) chat rows, newest first."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if limit > 0:
        cursor.execute("SELECT * FROM chats ORDER BY id DESC LIMIT ?", (limit,))
    else:
        cursor.execute("SELECT * FROM chats ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows


def search_chat(keyword: str):
    """Search chat history for a keyword in either user or bot column."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM chats WHERE user LIKE ? OR bot LIKE ?",
        (f"%{keyword}%", f"%{keyword}%")
    )
    results = cursor.fetchall()
    conn.close()
    return results


def clear_db():
    """Delete every row from the chats table."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chats")
    conn.commit()
    conn.close()
    print("[DB] All chat records deleted.")



# ─────────────────────────────────────────
#  COMMAND PROCESSOR
# ─────────────────────────────────────────
def process_command(query: str) -> bool:
    """
    Process user command. Returns False to quit.
    Every exchange is automatically saved to today's chat log.
    """
    if not query:
        return True

    response = ""  # Will hold Jarvis's reply text for logging

    # --- Clear chat history ---
    if "clear chat" in query or "clear history" in query:
        clear_chat()
        return True  # clear_chat speaks itself; no further logging needed

    # --- Time & Date ---
    elif "time" in query and "date" not in query:
        now = datetime.datetime.now()
        response = f"The current time is {now.strftime('%I:%M %p')}, {USER_NAME}."

    elif "date" in query or "today is" in query:
        now = datetime.datetime.now()
        response = f"Today is {now.strftime('%A, %B %d, %Y')}."

    # --- Wikipedia (prefix shortcut: "wiki <topic>") ---
    elif query.startswith("wiki "):
        import wikipedia
        topic = query[5:].strip()
        try:
            response = wikipedia.summary(topic, sentences=2)[:300]
        except wikipedia.exceptions.DisambiguationError as e:
            options = ", ".join(e.options[:3])
            response = f"Too many results for {topic}. Did you mean: {options}? Please be more specific."
        except Exception:
            response = f"Sorry, I couldn't retrieve information about {topic} right now."

    # --- Wikipedia (natural language) ---
    elif any(q in query for q in ["who is", "what is", "tell me about"]):
        import wikipedia
        topic = query
        for phrase in ["who is", "what is", "tell me about"]:
            topic = topic.replace(phrase, "")
        topic = topic.strip()
        try:
            response = wikipedia.summary(topic, sentences=2)[:300]
        except wikipedia.exceptions.DisambiguationError as e:
            options = ", ".join(e.options[:3])
            response = f"Too many results for {topic}. Did you mean: {options}? Please be more specific."
        except Exception:
            response = f"Sorry, I couldn't retrieve information about {topic} right now."

    # --- Web Browsing ---
    elif "open" in query:
        for site in ["youtube", "google", "gmail", "github", "stackoverflow"]:
            if site in query:
                open_website(site)
                response = f"Opening {site} for you, {USER_NAME}."
                break
        else:
            response = "Which website would you like me to open?"

    elif "search" in query:
        term = query.replace("search", "").replace("for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={term}")
        response = f"Searching Google for {term}."

    # --- Weather ---
    elif "weather" in query:
        city = query.split("in")[-1].strip() if " in " in query else "Chennai"
        get_weather(city)
        response = f"Fetched weather for {city}."

    # --- Entertainment ---
    elif "play music" in query or "music" in query:
        webbrowser.open("https://music.youtube.com")
        response = "Opening YouTube Music."

    elif "joke" in query:
        import random
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
            "Why did the AI break up with the internet? Too many connections!",
            "A SQL query walks into a bar and asks two tables: Can I join you?",
            "Why do Java developers wear glasses? Because they don't see sharp!",
        ]
        response = random.choice(jokes)

    # --- Notes ---
    elif "note" in query or "remember" in query:
        note = query.replace("take a note", "").replace("remember", "").strip()
        note = note if note else "Unspecified note"
        take_note(note)
        response = f"Note saved: {note}"

    # --- System ---
    elif "shutdown" in query or "shut down" in query:
        response = "Shutting down. Goodbye!"
        speak(response)
        save_chat(query, response)
        save_chat_db(query, response)
        os.system("shutdown /s /t 1" if os.name == "nt" else "shutdown -h now")
        return True

    # --- Exit ---
    elif any(w in query for w in ["exit", "quit", "goodbye", "bye", "stop"]):
        response = f"Goodbye, {USER_NAME}! Have a great day!"
        speak(response)
        save_chat(query, response)
        save_chat_db(query, response)
        return False

    # --- AI Fallback ---
    else:
        response = ask_ai(query)

    # Speak and log every response (text file + SQLite)
    if response:
        speak(response)
        save_chat(query, response)
        save_chat_db(query, response)

    return True


# ─────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────
def main():
    """Main function with optional test mode."""
    import sys
    
    # Check for test/demo mode
    test_mode = "--test" in sys.argv or "--demo" in sys.argv
    
    if test_mode:
        print("\n[TEST MODE] Running in demonstration mode without microphone")
        speak(f"{get_greeting()}, {USER_NAME}! I am {JARVIS_NAME}, your AI assistant.")
        speak("Demo mode: Type commands (or 'quit' to exit)")
        while True:
            try:
                query = input("\nYou: ").strip().lower()
                if not query:
                    continue
                if not process_command(query):
                    break
            except KeyboardInterrupt:
                speak(f"Shutting down. Goodbye {USER_NAME}!")
                break
            except Exception as e:
                print(f"[ERROR] {e}")
                continue
    else:
        speak(f"{get_greeting()}, {USER_NAME}! I am {JARVIS_NAME}, your AI assistant.")
        speak("How can I help you today?")

        try:
            while True:
                query = listen()
                if not process_command(query):
                    break
        except KeyboardInterrupt:
            speak(f"Shutting down. Goodbye {USER_NAME}!")
            print("\n[JARVIS stopped by user]")


if __name__ == "__main__":
    init_db()   # ✅ Create / verify chat.db before anything else
    main()
