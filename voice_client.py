import speech_recognition as sr
from gtts import gTTS
import streamlit as st

import os

def speak(text):
    tts = gTTS(text=text, lang='en-IN')
    filename = "output.mp3"
    tts.save(filename)
    audio_file = open(filename, 'rb')
    st.audio(audio_file.read(), format='audio/mp3')
    audio_file.close()
    os.remove(filename)

recognizer = sr.Recognizer()

def listen() -> str:
    with sr.Microphone() as source:
        st.write("🎙️ Listening... please speak")
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=7)
    try:
        text = recognizer.recognize_google(audio, language="en-IN")
        return text
    except Exception:
        return ""
