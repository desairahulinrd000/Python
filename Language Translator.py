from googletrans import Translator
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again Please...")
        speak("Say that again Please...")
        return "None"
    return query

def Translate():
    
    speak("Speak")
    sentence = takeCommand()
    trans = Translator()
    kannada="kannada"
    hindi="hindi"
    marathi="marathi"
    tamil="tamil"
    telugu="telegu"
    trans_sen = trans.translate(sentence,src='en',dest=kannada)
    print(trans_sen.text)
    speak(trans_sen.text)

while True:
    Translate()
