import random
import requests
import platform
import subprocess
import time
from PIL import ImageGrab

def extra_commands(query):
    query = query.lower()

    if 'weather' in query:
        speak("Please tell me the city name for weather.")
        city = listen_for_command()
        if city:
            get_weather(city)
        else:
            speak("City name not provided.")

    elif 'screenshot' in query:
        take_screenshot()

    elif 'motivate me' in query or 'motivation' in query:
        motivational_quote()

    elif 'set timer' in query:
        speak("For how many seconds?")
        sec = listen_for_command()
        if sec.isdigit():
            set_timer(int(sec))
        else:
            speak("Please provide a valid number.")

    elif 'system info' in query or 'system information' in query:
        system_info()

    elif 'open notepad' in query:
        open_notepad()

    elif 'open calculator' in query:
        open_calculator()

    elif 'fun fact' in query:
        tell_fun_fact()

    else:
        # If none of the new commands matched, do nothing or you can add a fallback here
        pass


# Helper functions used by extra_commands

def get_weather(city):
    WEATHER_API_KEY = 'your_openweathermap_api_key'  # replace with real key
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()
        if data.get("cod") != 200:
            speak("I couldn't find that city.")
            return
        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]
        speak(f"The temperature in {city} is {temp} degrees Celsius with {desc}.")
    except Exception as e:
        speak("Sorry, I couldn't get the weather information.")

def take_screenshot():
    try:
        img = ImageGrab.grab()
        filename = f"screenshot_{int(time.time())}.png"
        img.save(filename)
        speak(f"Screenshot saved as {filename}")
    except Exception as e:
        speak("Sorry, I couldn't take a screenshot.")

def motivational_quote():
    quotes = [
        "The best way to get started is to quit talking and begin doing.",
        "Don't let yesterday take up too much of today.",
        "It's not whether you get knocked down, it's whether you get up.",
        "If you are working on something exciting, it will keep you motivated.",
        "Success is not in what you have, but who you are."
    ]
    speak(random.choice(quotes))

def set_timer(seconds):
    speak(f"Setting a timer for {seconds} seconds.")
    time.sleep(seconds)
    speak(f"Timer for {seconds} seconds is done!")

def system_info():
    info = platform.platform()
    speak(f"Your system information: {info}")

def open_notepad():
    system = platform.system()
    try:
        if system == 'Windows':
            subprocess.Popen(['notepad.exe'])
            speak("Opening Notepad.")
        else:
            speak("Notepad opening is only supported on Windows.")
    except Exception as e:
        speak("Failed to open Notepad.")

def open_calculator():
    system = platform.system()
    try:
        if system == 'Windows':
            subprocess.Popen(['calc.exe'])
            speak("Opening Calculator.")
        else:
            speak("Calculator opening is only supported on Windows.")
    except Exception as e:
        speak("Failed to open Calculator.")

def tell_fun_fact():
    facts = [
        "Honey never spoils. Archaeologists found pots of honey in Egyptian tombs that are over 3000 years old and still edible.",
        "A day on Venus is longer than a year on Venus.",
        "Octopuses have three hearts.",
        "Bananas are berries, but strawberries are not.",
        "There are more stars in the universe than grains of sand on all the world's beaches."
    ]
    speak(random.choice(facts))

