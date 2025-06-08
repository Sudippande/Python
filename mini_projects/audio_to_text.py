import speech_recognition as sr
from pydub import AudioSegment

recognizer=sr.Recognizer()
audio_file="audiobook.wav"

AudioSegment.from_mp3(audio_file).export(audio_file,format="wav")
with sr.AudioFile(audio_file) as source:
    audio_data=recognizer.record(source)

try:
    text=recognizer.recognize_amazon(audio_data)
    print("Extracted text",text)
except sr.UnknownValueError:
    print("Could not understand the audio")
except sr.Recognizer as e:
    print("ApI error:",e)