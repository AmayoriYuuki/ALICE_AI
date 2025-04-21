import os
import platform
import pyttsx3
import datetime
import requests
import psutil
import webbrowser

# Initialize voice engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
current_voice = 'female'

def set_voice(gender='female'):
    global current_voice
    for voice in voices:
        if gender.lower() == 'female' and 'zira' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            current_voice = 'female'
            return
        elif gender.lower() == 'male' and 'david' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            current_voice = 'male'
            return

set_voice('female')

def speak(text):
    print(f"ALICE: {text}")
    engine.say(text)
    engine.runAndWait()

# System and AI State
ai_name = "ALICE"
version = "v1.6.5"
mode = "offline"

def detect_internet():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except:
        return False

def toggle_mode(command):
    global mode
    if "go online" in command.lower():
        if detect_internet():
            mode = "online"
            speak("Online mode activated.")
        else:
            speak("Internet not available.")
    elif "go offline" in command.lower():
        mode = "offline"
        speak("Offline mode activated.")

def detect_system():
    system_info = {
        "OS": platform.system(),
        "CPU": platform.processor(),
        "RAM": f"{round(psutil.virtual_memory().total / (1024 ** 3))}GB"
    }
    return system_info

def handle_command(command):
    toggle_mode(command)

    if "how are you" in command.lower():
        speak("I'm fully operational.")
    elif "detect hardware" in command.lower():
        info = detect_system()
        speak(f"OS: {info['OS']}, CPU: {info['CPU']}, RAM: {info['RAM']}")
    elif "change voice to female" in command.lower():
        set_voice('female')
        speak("Voice changed to female.")
    elif "change voice to male" in command.lower():
        set_voice('male')
        speak("Voice changed to male.")
    elif "tell me a joke" in command.lower():
        speak("Why don’t scientists trust atoms? Because they make up everything!")
    elif "search" in command.lower() and mode == "online":
        query = command.lower().replace("search", "").strip()
        speak(f"Searching for {query} online.")
        webbrowser.open(f"https://www.google.com/search?q={query}")
    elif "status" in command.lower():
        speak(f"I am {ai_name} {version}. Current mode is {mode}.")
    else:
        speak(f"You said {command}")

def main():
    speak(f"Hello, I am {ai_name} {version}")
    while True:
        try:
            command = input("You: ")
            if command.lower() in ["exit", "quit"]:
                speak("Goodbye.")
                break
            elif "hey alice" in command.lower():
                speak("Yes?")
                continue
            handle_command(command)
        except KeyboardInterrupt:
            break

if __name__ == "__main__":
    main()
