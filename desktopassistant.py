import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import speech_recognition as sr

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
    speak("I am your desktop assistant. Say 'Ankit' to wake me up.")

# Function to listen for any speech
def listen_for_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake word ('Ankit')...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
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
        speak("Yes, I'm listening.")
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
                os.system("taskkill /f /im chrome.exe")  # Only works on Windows with Chrome

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"The current time is {strTime}")

            elif 'joke' in query:
                joke = pyjokes.get_joke()
                speak(joke)

            elif 'chatgpt' in query:
                speak("Opening ChatGPT...")
                webbrowser.open("https://www.chatgpt.com/")

            elif 'exit' in query or 'bye' in query or 'quit' in query:
                speak("Goodbye! Have a nice day!")
                break

            else:
                speak("Sorry, I didn't understand that.")

# Ensure the assistant runs
if __name__ == "__main__":
    run_assistant()
