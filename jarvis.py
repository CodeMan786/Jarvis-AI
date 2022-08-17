import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!, sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!, sir!")   

    else:
        speak("Good Evening!, sir!")  

    speak("I am Jarvis. Please tell me how may, i help you!")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("now Listening you")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        speak("Recognizing and analyzing your order")    
        query = r.recognize_google(audio, language='en-in')
        print("User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("sorry, please Say that again!")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abdulaleemsiddiqui01@gmail.com', '123ali123#$')
    server.sendmail('abdulaleemsiddiqui01@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube')        
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("google.com")

        elif 'open flow' in query:
            speak('opening stack over flow')
            webbrowser.open("stackoverflow.com")  

        elif 'open git' in query:
            speak('opening git hub')
            webbrowser.open("github.com")        
         
        elif 'open facebook' in query:
            speak('opening facebook')
            webbrowser.open("facebook.com")

        elif 'who create you' in query:
            speak('sir, mr.Abdul Aleem created me')

        elif 'who are you' in query:
            speak('sir. I am Jarvis')


        elif 'open meet' in query:
            speak('opening google meet')
            webbrowser.open("meet.google.com")       


        elif 'play music' in query:
            music_dir = 'C:\Users\User\Music\Playlists'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {strtime}")



        elif 'open code' in query:
            speak('opening VS code')
            codePath = "E:\ali\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "kk2344758@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry sir. I am not able to send this email")    

