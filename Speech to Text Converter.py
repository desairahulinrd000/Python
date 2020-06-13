import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()



def get():
    
    r = sr.Recognizer()
    text=""

    with sr.Microphone() as source:
        print('Speak')
        speak("Speak")
        audio = r.listen(source)
        print("Done")
    try:
        text = r.recognize_google(audio)
        print('You said:\n' +text)
    except Exception as e:
        print(e) 

    file = open('output.txt','w')
    file.write(text)
    file.close()

while True:
    get()
    
