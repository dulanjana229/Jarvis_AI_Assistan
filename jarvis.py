import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui
import psutil
import pyjokes


engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)
    
def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)    
    speak("The current date is")    
    speak(date)    
    speak(month)    
    speak(year)
    
def wishme():
    speak("Welcome back sir")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Sir")
    elif hour >=12 and hour<18:
        speak("Good afternoon sir")
    elif hour >=18 and hour<24:
        speak("Good evening sir")
    else:
        speak("Good night sir")
    speak("Jarvis at your service. please tell me how can i help you?")  
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)    
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(query)        
        except Exception as e:
            print(e)
            speak("Say that again please....")        
            return "None"        
        return query
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gamil.com', 587)
    server.ehlo()
    server.starttls()
    server.login('dulanajanaanuraweera@gmail.com', '1234')
    server.sendmail('dulanajanaanuraweera@gmail.com', to, content)
    server.close()
    
def screenShot():
    img = pyautogui.screenshot()
    img.save("C:/Users/user/OneDrive/Pictures/Screenshots")

def cpu():
    usage = str(psutil.cpu_percent())
    speak('CPU is at'+ usage)
    battery = psutil.sensors_battery()
    speak('Battery is at')
    speak(battery.percent)

def jokes():
    speak(pyjokes.get_joke())

if __name__ == "__main__":
    wishme()
    while True:
        query = takeCommand().lower()
        
        if 'time' in query:
            time()
            
        elif 'date' in query:
            date()
            
        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)   
            
        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "dnadeeshan516@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
                
        elif 'search in chrome' in query:
            speak("What should I search?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe"
            search = takeCommand().lower()            
            wb.get(chromepath).open_new_tab(search + ".com")
            
        elif 'logout' in query:
            os.system("shutdown -l")
        elif 'shutdown' in query:
            os.system("shutdown /s /t 1")
        elif 'restart' in query:
            os.system("shutdown /r /t 1")
            
        elif 'play songs' in query:
            songs_dir = "C:/Users/user/Music"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir, songs[0]))
            
        elif 'remember that' in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("You told me to remember that" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
            
        elif 'do you know anything' in query:
            remember =open('data.txt', 'r')
            speak("You told me to remember that" + remember.read())
            
        elif 'screen shot' in query:
            speak("Taking screenshot")
            
        elif 'cpu' in query:
            cpu()
            
        elif 'joke' in query:
            jokes()
            
        elif 'offline' in  query:
            quit()



