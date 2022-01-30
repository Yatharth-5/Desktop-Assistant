



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
import pywhatkit
import time
import pygame
import playsound
import webbrowser
import pyaudio


brave_path = '"C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe" %s'
#webbrowser.get(chrome_path).open('http://docs.python.org/')
#import pyaudio
#k=True
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('rate',150)
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

first_time=True

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
    webbrowser.get(brave_path).open(str)


def speak(str):
    engine.say(str)
    print(str)
    engine.runAndWait()    

first_time=True

def take():
    '''This function takes input as speech and converts it into string'''
    '''
    if k==1:
        first_time=True
        k=k+1'''

    global first_time

    try:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshhold= 1 #it considers a 1 sec gap between a spoken text
            r.energy_threshhold= 4000 #(300) by default
            r.adjust_for_ambient_noise(source,duration=1)
            r.dynamic_energy_threshold=True
            audio = r.listen(source)
            #query=input()
            #stop()

        #k=1

        if(bool(first_time)==True):
            try:
                print("Recognizing...")
                query=r.recognize_google(audio,language='en-in')
                print(f"User said:{query}")
                query=query.lower()
                #speak("Command received")
                # if 'tell' or 'search' in query:
                #    wiki(query)
                if 'peter' in query:
                    speak("Listening my lord")
                
                if 'tell me' in query:
                    query.strip("tell me about")
                    speak(pywhatkit.info(query))
                    
                if 'open codeforces' in query:
                    web("codeforces.com")
                    
                if 'open whatsapp' in query:
                    web("web.whatsapp.com")
                    
                if 'stop' in query :
                    speak("Thank you for using me!!")
                    k=0
                if 'task manager' in query:
                    app("C:\\Windows\\system32\\Taskmgr.exe")
                if 'shut down' in query:
                    pywhatkit.shutdown(time=100)
                    speak("The system will shut down in 100 seconds")
                    speak("To cancel shutdown say, cancel shutdown")

                if 'cancel shutdown' in query:
                    pywhatkit.cancel_shutdown()

                if 'reminder' in query:
                    app("C:\\Users\\Admin\\PycharmProjects\\reminder\\main.py")
                if 'youtube' in query:
                    web("youtube.com")
                
                if 'play' in query:
                    query=query.strip("play ")
                    #query contains the name of the song to be played.
                # if 'youtube' in query:
                    #query=query.strip(" on youtube")

                    pywhatkit.playonyt(query,use_api=True)
                    speak(f"Sure, playing {query} on youtube")
                    
                if 'mar' in query:   
                    #speak_slow("Arre shubh shubh boliye...")  
                    playmusic("shubhshubh.mp3")
                    #print("hi")
                if 'translate' in query:
                    pass
                first_time=False

            except Exception as e:
                print(e)
                print("Say that again please...")
                #speak("Say that again please...")
                #return "None"
        '''
        while k==1:
            #print("hello, I am inside true block")
            take()'''


            #return query

    except Exception as e:
        print(e)
        time.sleep(10)



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
    k=True
    speak("Please let me know your sweet, kind and gracious name")

    naam=input()
    wishme(naam)
    take()


    #webbrowser.get(using='google-chrome')
    #web('youtube.com')
    #app("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Wordpad.lnk")
    #app("C:\\Users\\Admin\\AppData\\Local\\WhatsApp\\WhatsApp.exe")
    #app("C:\Windows\system32\Taskmgr.exe")
