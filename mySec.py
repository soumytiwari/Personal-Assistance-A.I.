import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!Kheera kaat ke...")
    elif(hour>=12 and hour<17):
        speak("Good Afternoon!")
    # elif(hour>=17 and hour<20):
    #     speak("Good Evening!")
    else:
        speak("Good Evening!")
    
    # ask if the person is male or female, according to that say sir/ma'am
    speak("I am your Secretery Jarvis. Kheera kaat ke.... My love, please tell me how may I help you. Kheera kaat ke...")

def takeCommand():
    '''It takes microphone input from the user and returns string output'''

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1   #experiment and more...:)
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)  #shows error
        print("Say that again please...")
        return "None"
    return query

# Not working properly
def sendEmail(to, content):
    #enable less secure sites first
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('idkbooze@gmail.com', 'New password')
    server.sendmail('idkbooze@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # speak("Hrishikesh let's study together")
    # takeCommand()
    while True:
        query=takeCommand().lower()
        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube music' in query:
            webbrowser.open("music.youtube.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        #his example of music directory, me makes than plays
        # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            # songs = os.listdir(music_dir)
            # print(songs)
            # os.startfile(os.path.join(music_dir, songs[0]))           //or use random module and play

        # elif 'open whataspp' in query:
        #     webbrowser.open("web.whatsapp.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, the time is: {strTime}")

        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/tiwarisoumya111/")

        elif 'open code' in query:
            codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open podcast' in query:
            webbrowser.open("podcasta.google.com")

        elif 'open classroom' in query:
            webbrowser.open("classroom.google.com")

        elif 'open one note' in query:
            notePath = "C:\Program Files\Microsoft Office\root\Office16\ONENOTE.EXE"
            os.startfile(notePath)

        elif 'open keep notes' in query:
            webbrowser.open("keep.google.com")

        elif 'open medium' in query:
            webbrowser.open("medium.com")

        elif 'open gmail' in query:
            webbrowser.open("mail.google.com")

        elif 'open drive' in query:
            webbrowser.open("drive.google.com")

        elif 'open adobe photo shop' in query:
            photoshopPath = "C:\Program Files\Adobe\Adobe Photoshop 2021\Photoshop.exe"
            os.startfile(photoshopPath)

        elif 'sexy jutsu' in query:
            webbrowser.open("https://music.youtube.com/watch?v=u14ybEqmlDw&list=RDAMPLOLAK5uy_kBBYBh2h1Vy0A93NHAU296nyQJjs2KfxY")
        
        elif 'naruto uzumaki' in query:
            webbrowser.open("https://music.youtube.com/watch?v=hxZaUm0JnUw&list=OLAK5uy_k0EHdMmS2Ja1KlacjfZS79vRqUWRSXTeM")

        # dictionary, value: emails and element: the one 
        elif 'email to me' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                #to = "harryyouremail@gmail.com" #take input by user
                to = "tiwarisoumya111@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend, I am not able to send this email.")

        elif 'quit' in query:
            exit(0)