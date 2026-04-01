import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr
import requests
import pyttsx3
import os
import re

from dotenv import load_dotenv
load_dotenv()

# 🔑 API KEY
api_key = os.getenv("API_KEY")

print("API KEY:", api_key)

# RECORD SETTINGS
fs = 44100
seconds = 5

print("say something...")

# RECORD AUDIO
recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, dtype='int16')
sd.wait()

# SAVE FILE
write("output.wav", fs, recording)

# SPEECH TO TEXT
r = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio = r.record(source)

text = r.recognize_google(audio)
print("You said:", text)

# CITY DETECTION

def extract_city(text):
    text = text.lower()

    patterns = [
        r"weather in (\w+)",
        r"temperature in (\w+)",
        r"in (\w+)",
        r"(\w+) weather",
        r"(\w+) ka mausam",
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1)

    return text.split()[-1]

city = extract_city(text)
print("Detected city:", city)

# WEATHER API CALL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)
data = response.json()

# ERROR CHECK
if data.get("cod") != 200:
    print("City not found")
    exit()

# DATA EXTRACT
temp = data["main"]["temp"]
desc = data["weather"][0]["description"]

# RESPONSE
response_text = f"{city} ka temperature {temp} degree celsius hai aur weather {desc} hai"
print(response_text)

# TEXT TO SPEECH
engine = pyttsx3.init()
engine.say(response_text)
engine.runAndWait()