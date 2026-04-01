# Voice-Based Weather Assistant

A Python-based voice-enabled weather assistant that accepts natural language input, extracts the city intelligently, fetches real-time weather data, and responds using text-to-speech.

---

## Features

* Voice input through microphone
* Intelligent city extraction from flexible sentences
* Real-time weather data using OpenWeather API
* Voice response using text-to-speech
* Supports natural queries such as:

  * "weather in delhi"
  * "aaj delhi ka mausam kaisa hai"
  * "delhi weather update"

---

## Tech Stack

* Python
* SpeechRecognition
* SoundDevice
* Pyttsx3
* Requests
* python-dotenv

---

## Installation

Clone the repository:
git clone https://github.com/ridhimagarg23/weather-cli-app.git

Navigate to the project folder:
cd weather-cli-app

Create virtual environment:
python -m venv venv

Activate environment:
venv\Scripts\activate

Install dependencies:
pip install sounddevice scipy SpeechRecognition pyttsx3 requests python-dotenv

---

## Setup

Create a `.env` file in the root directory:

API_KEY=your_api_key_here

---

## Usage

Run the assistant:

python voice_weather.py

---

## Example

Input:
Aaj Delhi ka mausam kaisa hai

Output:
Delhi ka temperature 32°C hai aur weather clear hai

---

## Error Handling

* Handles invalid or missing API key
* Handles incorrect city detection
* Prevents crashes using safe checks

---

## Future Improvements

* Wake word detection ("Hey Assistant")
* Continuous listening mode
* Multi-city handling
* Advanced NLP-based entity extraction

---

## Author

Ridhima Garg
