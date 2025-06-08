import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_cmd(command):
    command = command.lower()
    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook")
    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")
    elif "open github" in command:
        webbrowser.open("https://github.com")
        speak("Opening GitHub")
    elif command.startswith("play"):
        song = command.split(" ", 1)[1]
        if song in musiclib.music:
            webbrowser.open(musiclib.music[song])
            speak(f"Playing {song}")
        else:
            speak(f"Sorry, I don't have the song {song}")
    else:
        speak("I didn't understand the command.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word: Jarvis...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=6, phrase_time_limit=4)

            print("Recognizing wake word...")
            try:
                word = r.recognize_google(audio)
                print(f"You said: {word}")

                if word.lower() == "jarvis":
                    speak("Yes, how can I help?")
                    
                    with sr.Microphone() as source:
                        print("Listening for your command...")
                        r.adjust_for_ambient_noise(source, duration=1)
                        audio = r.listen(source, timeout=6, phrase_time_limit=6)
                        command = r.recognize_google(audio)
                        print(f"Command: {command}")
                        process_cmd(command)

            except sr.UnknownValueError:
                print("Could not understand wake word.")
            except sr.RequestError:
                speak("Sorry, speech service is not available.")
        except Exception as e:
            print(f"Error: {e}")
