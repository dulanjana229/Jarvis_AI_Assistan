import pyttsx3
import datetime
import speech_recognition as sr

# Initialize the speech engine
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f"The time is {current_time}")

def get_date():
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day    
    speak(f"Today's date is {day} {month} {year}")

def wish_me():
    speak("Welcome back, sir")
    speak("The current time is")
    get_time()
    speak("The current date is")
    get_date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good Morning, sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon, sir")
    elif hour >= 18 and hour < 24:
        speak("Good Evening, sir")
    else:
        speak("Good Night, sir")
    speak("Jarvis at your service. Please tell me how can I help you?")  
    
def take_command(language='en-IN'):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
            print("Done listening.")
        except Exception as e:
            print(f"Listening error: {e}")
            speak("I couldn't hear anything.")
            return "None"
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language=language)
        print(f"You said: {query}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
        speak("Sorry, I could not understand what you said.")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        speak("Sorry, I'm having trouble connecting to the service.")
        return "None"
    return query

def test_microphone():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for ambient noise, please wait...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening for 10 seconds...")
        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
            print("Done listening.")
        except Exception as e:
            print(f"Listening error: {e}")
            return

    try:
        print("Recognizing...")
        text = r.recognize_google(audio, language='en-IN')
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

# Example usage
wish_me()
command = take_command(language='en-IN')
print(f"Command received: {command}")

test_microphone()
