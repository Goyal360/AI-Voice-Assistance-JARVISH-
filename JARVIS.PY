import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!") 

    speak("I am Jrvis Sir. Please tell me how may I help you")

def takeCommand():
    #it takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print("Listening...")
        r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(sourse)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)

        print("Say again please...") 
        return "None"   
    return query 


def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('goyal.gaurav369@gmail.com', 'password')
    server.sendmail('goyal.gaurav369@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()

        #logic for executing tasks based on query 
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open w3school' in query:
            webbrowser.open("w3school.com")    

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'C:\\Users\\SS_HP\\Music'
            songs = os.listdir(music_dir)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"GAURAV SIR The Time is{strTime}")    

        elif 'open code' in query:
            codePath = "C:\\Users\\SS_HP\\AppData\\Local\\Programs\\Common\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)   

        elif 'send email to Gaurav' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "goyal.gaurav369@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Gaurav Sir. I am not able to send this email")  