import pyttsx3  # Text-to-Speech
import speech_recognition as sr  # Speech Recognition
import datetime  # Time & Date
import wikipedia  # Wikipedia Search
import webbrowser  # Open Webpages
import os  # Open Applications
import requests  # API Requests (For Weather & NASA)
import pyjokes  # Fetch Jokes

# Initialize Speech Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I assist you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Could not understand, please say that again...")
        speak("Could not understand, please say that again...")
        return "None"
    return query.lower()

def open_website(url, name):
    speak(f"Opening {name}")
    webbrowser.open(url)

def search_wikipedia(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def play_music():
    music_dir = "YOUR_MUSIC_DIRECTORY"
    songs = os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[0]))

def get_time():
    str_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"The time is {str_time}")

def get_date():
    today = datetime.datetime.today().strftime('%Y-%m-%d')
    speak(f"Today's date is {today}")

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)

def get_weather():
    API_KEY = "YOUR_OPENWEATHER_API_KEY"
    CITY = "YOUR_CITY"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()
    if response["cod"] != "404":
        main = response["main"]
        temperature = main["temp"]
        weather_desc = response["weather"][0]["description"]
        speak(f"The current temperature in {CITY} is {temperature} degrees Celsius with {weather_desc}.")
    else:
        speak("Sorry, I couldn't fetch the weather data.")

def open_application(app_path, app_name):
    speak(f"Opening {app_name}")
    os.startfile(app_path)

def main():
    wish_me()
    while True:
        query = take_command()
        
        if 'wikipedia' in query:
            search_wikipedia(query)
        elif 'open youtube' in query:
            open_website("https://youtube.com", "YouTube")
        elif 'open google' in query:
            open_website("https://google.com", "Google")
        elif 'open facebook' in query:
            open_website("https://facebook.com", "Facebook")
        elif 'open github' in query:
            open_website("https://github.com", "GitHub")
        elif 'play music' in query:
            play_music()
        elif 'time' in query:
            get_time()
        elif 'date' in query:
            get_date()
        elif 'joke' in query:
            tell_joke()
        elif 'weather' in query:
            get_weather()
        elif 'open vscode' in query:
            open_application("YOUR_VSCODE_PATH", "VS Code")
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
