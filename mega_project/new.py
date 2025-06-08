import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib

r = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()

def process_cmd(c):
    c = c.lower()

    if "open google" in c:
        speak("Opening Google...")
        webbrowser.open("https://google.com")

    elif "open facebook" in c:
        speak("Opening Facebook...")
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c:
        speak("Opening YouTube...")
        webbrowser.open("https://youtube.com")

    elif "open github" in c:
        speak("Opening GitHub...")
        webbrowser.open("https://github.com")

    elif c.startswith("play"):
        song = c.split(" ")[1]  # play <song>
        if song in musiclib.music:
            link = musiclib.music[song]
            speak(f"Playing {song}")
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't have the song {song} in my library.")

    else:
        speak("Sorry, I didn't understand the command.")

def listen_for_wake_word():
    try:
        with sr.Microphone() as source:
            print("Listening for 'Jarvis'...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            word = r.recognize_google(audio)
            print(f"You said: {word}")
            return word.lower()
    except sr.UnknownValueError:
        print("Didn't catch that.")
    except sr.RequestError:
        print("API unavailable or network error.")
    except Exception as e:
        print(f"Error: {e}")
    return ""

def listen_for_command():
    try:
        with sr.Microphone() as source:
            speak("I'm listening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=6, phrase_time_limit=6)
            command = r.recognize_google(audio)
            print(f"Command: {command}")
            return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
    except sr.RequestError:
        speak("Speech recognition service is down.")
    except Exception as e:
        print(f"Error: {e}")
    return ""

# Main Loop
if __name__ == "__main__":
    speak("Jarvis initialized and listening...")

    while True:
        wake_word = listen_for_wake_word()
        if "jarvis" in wake_word:
            speak("Yes?")
            command = listen_for_command()
            process_cmd(command)
