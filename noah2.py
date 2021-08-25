



'''
1. Alarm
2. Send and Speak Whatsapp/ Instagram msgs
3. Schedule msgs
4. Open apps like google/ meet/ mail/ classroom/ Games/ website
5. Open reminder file
6. Close an application
7. Listen by its name
8. Search for an app in pc
9. Connect to wifi/ bt
10. Play songs/ movies
11. Who are you? Who created you?
12. Type and listen both
13. Timetable scheduler
14. Shut down pc
15. Automatically start at boot time
16. Automatically refresh the pc and notify
17. Lists every task on "What can you do for me?"
18. Open Task Manager
'''


import pyttsx3   #text to speech conversion library
import datetime
import speech_recognition as sr
import wikipedia
import os
import time
import pygame
from pygame import mixer
from playsound import playsound
import webbrowser
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#webbrowser.get(chrome_path).open('http://docs.python.org/')
#import pyaudio
k=True
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def wiki(query):
    speak("Searching")
    query=query.replace('tell me about','')
    results=wikipedia.summary(query,sentences=2)
    speak("According to wikipedia")
    speak(results)

def app(str):
    #print(f"Opening {str}")
    speak("I am doing that, please wait")
    os.startfile(str)
    target="Aru jio"


def playmusic(song):
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(0)
    time.sleep(4)

def web(str):
    speak("Just doing that!!")
    webbrowser.get(chrome_path).open(str)


def speak(str):
    engine.say(str)
    print(str)
    engine.runAndWait()

def take():
    '''This function takes input as speech and converts it into string'''
    k=True
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshhold: 1 #it considers a 1 sec gap between a spoken text
        r.energy_threshhold: 300
        
        audio = r.listen(source)
        #query=input()
        #stop()

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}")
        #speak("Command received")
        #if 'tell' or 'search' in query:
         #   wiki(query)
        if 'Peter' in query:
            speak("Listening my lord")
        
        elif 'open codeforces' in query:
            web("codeforces.com")
            
        if 'open Whatsapp' in query:
            #app("C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
            web("web.whatsapp.com")
            
        elif 'stop' in query :
            speak("Thank you for using me!!")
            k=False
        elif 'task manager' in query:
            app("C:\\Windows\\system32\\Taskmgr.exe")
        elif 'shut down' in query:
            pass
        elif 'reminder' in query:
            app("C:\\Users\\Admin\\PycharmProjects\\reminder\\main.py")
        elif 'YouTube' in query:
            web("youtube.com")
        elif 'Play' in query:
            web("https://gaana.com/")
        elif 'Mar' in query:
            playsound("shubhshubh.mp3")
            #speak("Arre shubh shubh boliye...")       
        

    except Exception as e:
        #print(e)
        print("Say that again please...")
        #speak("Say that again please...")
        #return "None"
    
    while k==True:
          #print("hello, I am inside true block")
          take()


    return query




def wishme(naam):
    hour=int(datetime.datetime.now().hour)
    print(hour)
    if(hour>=0 and hour<12):
        speak(f"Good morning {naam}")
    elif hour>=12 and hour<=15:
        speak(f"Good afternoon {naam}")
    elif hour>=16 and hour<24:
        speak(f"Good evening {naam}")

    speak("I am Peter, please tell me how can I be of help!")





if __name__ == '__main__':
    speak("Please let me know your sweet, kind and gracious name")

    naam=input()
    if naam == "poonam" or naam=="arushi":
        g="mam"
    else:
        g="sir"
    wishme(naam)
    #wishme("Yatharth")
    take()
    #webbrowser.get(using='google-chrome')
    #web('youtube.com')
    #app("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Wordpad.lnk")
    #app("C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    #app("C:\Windows\system32\Taskmgr.exe")