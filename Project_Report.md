# JARVIS AI AGENT - Project Report

## 1. Introduction
The **JARVIS AI Agent** is an advanced, voice-activated virtual assistant inspired by Iron Man's JARVIS. Designed to streamline daily tasks, it integrates natural language processing, external API services, and a sleek web-based user interface to provide an interactive and responsive user experience. This project serves as a comprehensive college project demonstrating the integration of modern AI models with traditional software automation.

## 2. System Architecture
The project is divided into two main components:

### Backend Engine (`jarvis.py`)
The core Python engine acts as the central processor for the AI. It orchestrates:
- **Speech-to-Text**: Using the `SpeechRecognition` library to capture voice commands from the user's microphone.
- **Text-to-Speech**: Utilizing `pyttsx3` to provide audible, natural-sounding responses.
- **Command Routing**: Analyzing commands to trigger local functions or route complex questions to the AI brain.

### Frontend Web UI (`jarvis-ui/`)
A modern, visually striking web dashboard built with React and Vite.
- Implements a premium glassmorphism design.
- Features a CSS-animated "Arc Reactor" visualizer that reacts to the system's state.
- Utilizes custom React Hooks (`useSpeech.js`) to potentially bridge voice interaction with the visual frontend.

## 3. Core Features

### 🧠 Intelligent Conversational AI
Integration with the **Google Gemini API** (Gemini 2.5 Flash model) empowers Jarvis to answer general questions, brainstorm ideas, and maintain a conversational fallback when a command isn't explicitly hardcoded.

### 🌐 Web Automation & Browsing
Automated execution of browser tasks:
- Opening frequently used platforms (YouTube, Github, StackOverflow, Gmail).
- Querying Wikipedia and reading summaries aloud.
- Launching direct Google searches.

### 🌤️ Live Data Retrieval
Jarvis is connected to the OpenWeatherMap API, enabling real-time weather updates, temperature, and humidity readings for any specified city.

### 🛠️ System Utilities
- **Time & Date Tracking**: Real-time auditory reporting of the current date and time.
- **Note Taking**: Saving user-dictated notes into a local `jarvis_notes.txt` file for later review.
- **System Control**: Capabilities to shut down the host PC securely.

## 4. Technology Stack
- **Programming Languages**: Python 3, JavaScript (ES6+), HTML5, CSS3
- **Frontend Framework**: React 19 (via Vite)
- **AI & NLP**: Google Generative AI (Gemini), `SpeechRecognition` 
- **Voice Synthesis**: `pyttsx3`
- **External Web APIs**: OpenWeatherMap API, Wikipedia

## 5. Conclusion
The JARVIS AI Agent demonstrates a practical and impressive implementation of Large Language Models integrated with local automation. By coupling a highly capable Python backend with a premium React-based frontend, the system functions not just as a script, but as an immersive virtual assistant experience.
