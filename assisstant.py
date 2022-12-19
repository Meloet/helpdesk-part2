import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Melo")
    elif hour>=12 and hour<=16:
        speak("Good Afternoon Melo")
    elif hour>=16 and hour<=23:
        speak("Good Evening Melo")
    speak("How can I help you?")
def take():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio, language="en-in")
        print("Said " + query)
        return query
    except Exception as e:
        print("Enter your message")
        return "None"
if(__name__=='__main__'):
    wishme()
    while True:
        query=take().lower()
        if "wikipedia" in query:
            speak("Searching Wikipedia")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=6)
            speak("According to wikipedia")
            print(results)
            speak(results)