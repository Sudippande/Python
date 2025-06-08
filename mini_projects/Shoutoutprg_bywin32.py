# Write a program  to pronounce list of names using pyttsx3.
l=['sudip','Ram','Lakhan','khadga']
# import pyttsx3 as p
# engine=p.init()
# for i in l:
#     print(f"shoutout to: {i}")
#     engine.say(f"Shoutout to {i}")
#     engine.runAndWait()


# Write  a program to pronounce list of name using win32 api
import win32com.client
#initialize the text to speech engine
# speaker=win32com.client.Dispatch("SAPI.SpVoice")
# for name in l:
#     print(f"Shoutout to:{name}")
#     speaker.Speak(f"ShoutOut to :{name}")