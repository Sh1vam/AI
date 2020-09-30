import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import pyautogui # pip install pyautogui
import win32api,time,win32con,random

'print command is more use ful than type commmand'

def AI():
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
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
        speak(" Hello I am Jarvis .")       

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

    if __name__ == "__main__":
        wishMe()
        while True:
        # if 1:
            query = takeCommand().lower()
            if 'print' in query :
                #a=str(query)
                print(query[6:]+"\n")
                pyautogui.keyDown(query[6:])
                pyautogui.typewrite(query[6:])
            elif 'speak' in query:
                speak("please give me the input")
                x=input("INPUT A WORD : ")
                speak(x)
            elif 'type' in query:
                print(query[5:]+"\n")
                typethis(query[5:])
 
try:
    AI()
except:
    AI()
else:
    AI()
finally:
    AI()
