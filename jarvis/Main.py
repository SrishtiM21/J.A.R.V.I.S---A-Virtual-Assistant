import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import smtplib
import random
import antigravity
import os
import datetime
from playsound import playsound
import subprocess as sp
import requests
import pywhatkit as kit
from email.message import EmailMessage
from decouple import config



paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
}




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    print(f": {audio}")
    print("  ")
    engine.runAndWait()


def wishMe():
    speak("Initializing Jarvis")
    speak("Starting all systems applications")
    speak("Installing and checking all drivers")
    speak("Caliberating and examining all the core processors")
    speak("Checking the internet connection")
    speak("Wait a moment mam")
    speak("All drivers are up and running")
    speak("All systems have been activated")
    speak("Now I am online")
   
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        a = "Good Morning" , "hello", "Good Morning its a new day"
        speak(random.choice(a))

    elif hour>=12 and hour<18:
        b= "Good Afternoon!", "Good Afternoon! starting fresh"
        speak(random.choice(b))   

    else:
        c= "Good Evening!","Good Evening! welcomeback again"
        speak(random.choice(c)) 
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Currently it is {strTime}")
    speak("I am Jarvis. Online and ready mam. Please tell me how may I help you")
 
       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        speak("Say that again please...")  
        return "None"
    return query

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        speak("Say that again please...")  
        return "None"
    return query
    

def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)

def open_notepad():
    os.startfile(paths['notepad'])


def open_cmd():
    os.system('start cmd')

def open_calculator():
    sp.Popen(paths['calculator'])

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

def SpeedTest1():
    import speedtest
    speak("checking speed.....")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    speak(f"the downloading speed is {correctDown} mbps")
    return correctDown

def SpeedTest2():
    import speedtest
    speak("checking speed.....")
    speed = speedtest.Speedtest()
    uploading = speed.upload()
    correctUpload = int(uploading/800000)
    speak(f"the uploading speed is {correctUpload} mbps")
    return correctUpload

def internetspeed():
    import speedtest
    speak("checking speed.....")
    speed = speedtest.Speedtest()
    downloading = speed.download()
    correctDown = int(downloading/800000)
    uploading = speed.upload()
    correctUpload = int(uploading/800000)
    speak(f"the uploading speed is {correctUpload} mbps and the downloading speed is {correctDown} mbps")


def taskexe():
    
     while True:
        query = takeCommand().lower()

            
        if 'open google' in query:
                webbrowser.open("google.com")

        elif 'open stack overflow' in query:
                webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
                music_dir = 'C:\\Users\\Pratiksha\\Desktop\\songs'
                songs = os.listdir(music_dir)
                print(songs)   
                os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Mam, the time is {strTime}")

        elif 'open code' in query:
                codePath = "C:\\Users\\Pratiksha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
                    

        elif 'open notepad' in query:
                open_notepad()

    
        elif 'open command prompt' in query or 'open cmd' in query:
                open_cmd()

        elif 'open camera' in query:
                open_camera()

        elif 'open calculator' in query:
                open_calculator()


        elif 'wikipedia' in query:
                speak('What do you want to search on Wikipedia, mam?')
                search_query = input().lower()
                results = search_on_wikipedia(search_query)
                speak(f"According to Wikipedia, {results}")
               

        elif 'youtube' in query:
            speak('What do you want to play on Youtube, mam?')
            video = input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google, mam?')
            query = input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message mam? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message mam?")
            message = input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message mam.")

                
        elif 'joke' in query:
            speak(f"Hope you like this one mam")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen mam.")
            print(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, mam")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen mam.")
            print(advice)
                
        elif 'uploading speed' in query:
            SpeedTest2()                
        elif 'downloading speed' in query:
            SpeedTest1()

        elif 'internet speed' in query:
            internetspeed()

    
        elif 'introduce' in query:
            speak(" I am a fictional character in the Marvel Cinematic Universe film franchise. But I can be your personal Voice-Based AI Assistant. Developed in Python Programming Language. You can Add New Unique Features to me and Automate Tasks with just One Voice Command. Try me, you wont regret it!")  
if __name__ == "__main__":
    wishMe()
    taskexe()
