import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except Exception as e:
        print("Error:", e)

# Test speech output
speak("Hello! Testing voice output.")

# Test microphone input
speak("Say something.")
listen()
