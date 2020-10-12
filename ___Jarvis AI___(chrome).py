import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import pyautogui # pip install pyautogui
import smtplib
import requests as r
from PIL import Image
from PyPDF2 import*
import time
import win32api,time,win32con,random

def AI():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    # it will open chrome browser register your browser and path here
    webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"))

    def pdfmerge():

        import Browse
        import PDFMerg as PM
        import Merger as M

        PM.replace('PDFMerg.txt','/','\\\\')
        print("\nPath of Your File\n", PM.read())
        print('''\nExample:= "C:\\Users\\Shivam\\Downloads\\CamScanner 07-28-2020 13.22.15.pdf","D:\\Users\\Shivam\\Downloads\\New Doc 2020-07-21 19.27.15.pdf" ''')
        print("\nNote := The file In C Drive will be First And file in D drive will be Second")
        print('''\nExample (only for one file):= "C:\\Users\\Shivam\\Downloads\\CamScanner 07-28-2020 13.22.15.pdf",''')
        print("\nNote:= Protected Pdf Need To Be Decrepted First By User")
        print("\nNote:= if u are running it in terminal and path is too long copy it from text file which will open now")
        time.sleep(3)
        os.startfile('PDFMerg.txt')
        print("\n Any Error Will Exit The Program")
        print("\n You Can Change the order of PDF Files to be Merged")
        print(' remove "", or " ", from Path Pasted ')
        M.merger()
        speak("done")
    def image(x):
        try:
            img = Image.open('files\\'+x+'.png')
            img.save('files\\'+ x + ' .ico')
        except OSError:
            print("Image file extension is only valid")
            speak("Image file extension is only valid")
            image()
        finally:
            print("done")
            speak("done")
    def covid():
        speak("covid 19 information")
        d=r.get("https://api.covid19india.org/data.json")
        re=d.json()
        x=input("Enter State : ")
        t=re['statewise']
        for i in t:
            if str(i['state']).upper()==x.upper():
                print(i['state']+"::")
                speak(i['state']+"::")
                print("Confirmed Cases : "+ i["confirmed"])
                speak("Confirmed Cases : "+ i["confirmed"])
                print("Active Cases : "+ i["active"])
                speak("Active Cases : "+ i["active"])
                print("Deaths : "+ i["deaths"])
                speak("Deaths : "+ i["deaths"])
                print("Recovered Cases : "+ i["recovered"])
                speak("Recovered Cases : "+ i["recovered"])

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    

    def typethis(sentence=None,shift=False,control=False,delay=0.05,random_delay=0.05):
        for letter in sentence:
            time.sleep(random.random()*random_delay) # Makes it look like real typing
            c=letter
            punctflag = True
            if (letter>='A' and letter<='Z') or shift:
                win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                punctflag = False
            if letter>='a' and letter<='z':
                c=letter.upper()
                punctflag = False
            if ((letter>='0' and letter<='9') or (letter==' ')):
                punctflag=False
            if control:
                win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)

            if not punctflag: # Do this for real letters on the keyboard
                if isinstance(letter,(int)):
                    ordletter=letter
                else:
                    ordletter=ord(c)

                win32api.keybd_event(ordletter, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0) 
                time.sleep(delay)
                win32api.keybd_event(ordletter, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                            win32con.KEYEVENTF_KEYUP, 0)
                time.sleep(delay)

                if control:
                    win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
                if (letter>='A' and letter<='Z') or shift:
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
            # This must be some punctuation - try to deal with it. 
            # win32con doesn't include OEM
            else: 
                if letter=='.':
                    win32api.keybd_event(190, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(190, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                    win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                elif letter==',':
                    win32api.keybd_event(188, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(188, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                    win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                elif letter=='-':
                    win32api.keybd_event(189, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(189, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                    win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                elif letter=='?':
                    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(191, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(191, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                    win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                elif letter=='!':
                    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(ord('1'), 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(ord('1'), 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                    win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                elif letter=='>':
                    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(190, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(190, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                    win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                elif letter=='<':
                    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(188, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(188, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                    win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                elif letter=='~':
                    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(192, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(192, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                    win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                elif letter=='(':
                    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(ord('9'), 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(ord('9'), 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                    win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                elif letter==')':
                    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(ord('0'), 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(ord('0'), 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                    win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                elif letter=='+':
                    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(107, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(107, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                    win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                elif letter=='/':
                    win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(111, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                    time.sleep(delay)
                    win32api.keybd_event(111, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                    win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)
                    win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                    time.sleep(delay)


        win32api.keybd_event(13, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0) 
        # There is a carriage return at the end of each newline
        
        if delay>0.0:
            time.sleep(delay)
            win32api.keybd_event(13, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
            win32con.KEYEVENTF_KEYUP, 0)

    '''def typefromfile(filename):
        with open(filename, 'r') as fopen: # with automatically closes the file
            for line in fopen:
                typethis(line)

    time.sleep(3)'''  # switch focus to a target window manually in this time.

    # Edit below this point to change what it types. 
    # Supports lowercase and uppercase letters,
    # numbers, and . , - ! ? (depending on your keyboard layout)

    #typethis("What is happening?")

    #typefromfile("C:/Users/User/Desktop/ghost.txt")

    #typethis("all this should be in capslock", shift=True)

    def wishMe():
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            speak("Good Morning!")

        elif hour>=12 and hour<18:
            speak("Good Afternoon!")   

        else:
            speak("Good Evening!")  

        speak("I am Jarvis . Please tell me how could I help you")       

    def takeCommand():
        #It takes microphone input from the user and returns string output

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
            # print(e)    
            print("Say that again please...")  
            return "None"
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('youremail@gmail.com', 'your-password')
        server.sendmail('youremail@gmail.com', to, content)
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
                speak("opening youtube")
                webbrowser.get('chrome').open("youtube.com")

            elif 'open google' in query:
                speak("opening google")
                webbrowser.get('chrome').open("google.com")   

            elif 'play music' in query:
                speak("plating music")
                music_dir = 'Songs\\'
                songs = os.listdir(music_dir)
                print(songs)    
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Hello, the time is {strTime}")

            elif 'open' in query:
                    codePath = ('files\\')
                    a=str(query)
                    speak("opening "+a)
                    os.system('"'+str(codePath+str(a[5:])+".py"+'"'))

            elif 'email to ' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = '"'+query[9:]+'"'    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry my friend xyzw. I am not able to send this email")
            elif 'search' in query :
                a=str(query)
                b=a[7:]
                speak("searching "+b) 
                webbrowser.get('chrome').open(b)
            elif 'refresh' in query :
                speak("refreshing.......")
                AI()

            elif 'are you there' in query :
                speak("Yes I am There")
            elif 'print' in query :
                #a=str(query)
                print(query[6:]+"\n")
                pyautogui.keyDown(query[6:])
                pyautogui.typewrite(query[6:])
            elif 'covid' in query :
                a=str(query)
                print(a[6:])
                covid()
            elif 'png to icon' in query :
                a=str(query)
                print(a[12:])
                image(a[12:])
            elif 'merge' in query:
                pdfmerge()
            elif 'speak' in query:
                speak("please give me the input")
                x=input("INPUT A WORD : ")
                speak(x)
            elif 'type' in query:
                print(query[5:]+"\n")
                typethis(query[5:])
            elif 'start chrome' in query:
                speak("starting chrome")
                os.startfile("C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
            elif 'start firefox' in query:
                speak("starting firefox")
                os.startfile("C:\Program Files\Mozilla Firefox\Firefox.exe")
            elif 'start notepad' in query:
                speak("starting notepad")
                os.system("Notepad")
            elif 'start explorer' in query:
                speak("starting explorer")
                os.startfile("C:\Windows\Explorer.exe")
            elif 'start wordpad' in query:
                speak("starting wordpad")
                os.startfile("C:\Program Files\Windows NT\Accessories\wordpad.exe")
            elif 'start paint' in query:
                speak("starting paint")
                os.startfile("C:\Windows\System32\mspaint.exe")
            elif 'start command prompt' in query:
                speak("starting command prompt")
                os.startfile("C:\Windows\System32\cmd.exe")
            elif 'start control pannel' in query:
                speak("starting control pannel")
                os.startfile("C:\Windows\System32\control.exe")
            elif 'start winrar' in query:
                speak("starting winrar")
                os.startfile("C:\Program Files\WinRAR\WinRAR.exe")
            elif 'start winzip' in query:
                speak("starting winzip")
                os.startfile("C:\Program Files (x86)\WinZip\WINZIP32.EXE")
            elif 'start calculator' in query:
                speak("starting calaulator")
                os.startfile("C:\Windows\system32\calc.exe")
            elif 'play video' in query:
                speak("plating video")
                video_dir = 'Videos\\'
                videos = os.listdir(video_dir)
                print(videos)    
                os.startfile(os.path.join(video_dir, videos[0]))
            
            
                
try:
    AI()
except:
    AI()
else:
    AI()
finally:
    AI()
