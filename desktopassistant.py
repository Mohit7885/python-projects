import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import speech_recognition as sr
from PIL import ImageGrab
import time
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import random

# Text-to-speech function
def speak(text):
    print(f"Assistant: {text}")
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        print("Speech output not supported in this environment.")

# Greet user based on current time
def wish_user():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning!")
    elif hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Boss, how can I help you?")

# Function to listen for any speech
def listen_for_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake word ('Ankit')...")
        recognizer.adjust_for_ambient_noise(source, duration=0.1)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        speak("Speech recognition service is unavailable.")
        return ""

# Function to listen for a command after wake word
def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Yes Boss.")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print(f"Command received: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that.")
        return ""
    except sr.RequestError:
        speak("Speech service is currently unavailable.")
        return ""

# Screenshot function
def take_screenshot():
    try:
        img = ImageGrab.grab()
        filename = f"screenshot_{int(time.time())}.png"
        img.save(filename)
        speak(f"Screenshot saved as {filename}")
    except Exception as e:
        speak("Sorry, I couldn't take a screenshot.")

# Volume control functions using pycaw
def get_volume_interface():
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume

def mute_volume():
    volume = get_volume_interface()
    volume.SetMute(1, None)

def unmute_volume():
    volume = get_volume_interface()
    volume.SetMute(0, None)

def raise_volume():
    volume = get_volume_interface()
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = min(current_volume + 0.1, 1.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    speak(f"Volume raised to {int(new_volume * 100)} percent.")

def lower_volume():
    volume = get_volume_interface()
    current_volume = volume.GetMasterVolumeLevelScalar()
    new_volume = max(current_volume - 0.1, 0.0)
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    speak(f"Volume lowered to {int(new_volume * 100)} percent.")

# Main assistant loop
def run_assistant():
    wish_user()
    while True:
        wake_query = listen_for_speech()

        if 'ankit' in wake_query:
            query = listen_for_command()

            if query == "":
                continue

            if 'search' in query or 'wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "").replace("search", "")
                try:
                    result = wikipedia.summary(query, sentences=2)
                    speak("According to Wikipedia:")
                    speak(result)
                except:
                    speak("Sorry, I couldn't find anything.")

            elif 'open youtube' in query:
                speak("Opening YouTube...")
                webbrowser.open("https://www.youtube.com/")

            elif 'open google' in query:
                speak("Opening Google...")
                webbrowser.open("https://www.google.com/")

            elif 'close google' in query or 'close chrome' in query:
                speak("Closing Chrome browser...")
                os.system("taskkill /f /im chrome.exe")

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {strTime}")

            elif 'date' in query:
                today = datetime.date.today().strftime("%B %d, %Y")
                speak(f"Today's date is {today}")

            elif 'day' in query:
                day = datetime.datetime.now().strftime("%A")
                speak(f"Today is {day}")

            elif 'joke' in query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'fun fact' in query:
                facts = [
                    "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible.",
                    "Octopuses have three hearts and blue blood.",
                    "Bananas are berries, but strawberries are not.",
                    "A bolt of lightning contains enough energy to toast 100,000 slices of bread.",
                    "Sharks existed before trees."
                ]
                speak(random.choice(facts))

            elif 'chatgpt' in query:
                speak("Opening ChatGPT...")
                webbrowser.open("https://www.chatgpt.com/")

            elif 'weather' in query:
                speak("Showing current weather in your browser.")
                webbrowser.open("https://www.google.com/search?q=weather")

            elif 'screenshot' in query:
                take_screenshot()

            elif 'mute' in query:
                mute_volume()
                speak("Muting volume.")

            elif 'unmute' in query:
                unmute_volume()
                speak("Unmuting volume.")

            elif 'raise volume' in query or 'increase volume' in query:
                raise_volume()

            elif 'lower volume' in query or 'decrease volume' in query:
                lower_volume()

            elif 'open notepad' in query:
                speak("Opening Notepad...")
                os.system("notepad")

            elif 'open command prompt' in query or 'open cmd' in query:
                speak("Opening Command Prompt...")
                os.system("start cmd")

            elif 'lock' in query:
                speak("Locking the computer...")
                os.system("rundll32.exe user32.dll,LockWorkStation")

            elif 'shutdown' in query:
                speak("Shutting down the system...")
                os.system("shutdown /s /t 1")

            elif 'restart' in query:
                speak("Restarting the system...")
                os.system("shutdown /r /t 1")

            elif 'log out' in query or 'logout' in query:
                speak("Logging out...")
                os.system("shutdown -l")

            elif 'exit' in query or 'bye' in query or 'quit' in query:
                speak("Goodbye! Have a nice day!")
                break

            else:
                speak("Sorry, I didn't understand that.")

if __name__ == "__main__":
    run_assistant()
