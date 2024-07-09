import speech_recognition as sr
import webbrowser
import os
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return ""

def open_website(command):
    sites = {
        "youtube": "https://www.youtube.com",
        "wikipedia": "https://www.wikipedia.com"
    }
    for site, url in sites.items():
        if f"open {site}" in command.lower():
            say(f"Opening {site}, sir")
            webbrowser.open(url)
            return True
    return False

def open_application(app_name):
    if app_name.lower() == "this pc":
        os.startfile("explorer.exe")
        say("Opening This PC")
        return True
    elif app_name.lower() == "notepad":
        os.startfile("notepad.exe")
        say("Opening Notepad")
        return True
    elif app_name.lower() == "calculator":
        os.startfile("calc.exe")
        say("Opening Calculator")
        return True
    elif app_name.lower() == "camera":
        os.startfile("microsoft.windows.camera:")
        say("Opening Camera")
        return True
    # Add more applications as needed
    return False

def interpret_command(command):
    greetings = ["hello", "hi", "hey"]
    for greeting in greetings:
        if greeting in command.lower():
            say("Hello, I am fine.")
            return
    
    if "who created you" in command.lower():
        say("I was created by Aj.")
        return
    
    if open_website(command):
        return
    if open_application(command):
        return
    say(command)

if __name__ == '__main__':
    print('Good Morning Sir')
    say("Hello, I am Pulse A.I.")
    while True:
        text = takeCommand()  # Capture the command first
        if text:
            interpret_command(text)
