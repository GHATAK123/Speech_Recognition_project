import pyttsx3 # pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import webbrowser # pip install webbrowser
import os
import smtplib # pip install smtplib


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()
def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour >=0 and hour<12:
		speak("Good Morning Sir!")
	elif hour >= 12 and hour <18:
		speak("Good Afternoon Sir!")
	else:
		speak("Good Evening Sir!")
	speak("I am jarvis. Please tell me how can i help you.")
    	





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
        speak("I didn't catch that. What did you say?")
            
        print("I didn't catch that. What did you say?")  
        return "None"
    return query
def user(query):
    
    speak(f"Hii, {query}\n")
    #speak(f"Nice to meet {q}")        
		
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('eea58514@gmail.com','***********')
    server.sendmail('eea58514@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    speak("What is your name, Sir")
    query=takeCommand()
    n=query
    user(query)
    while True:
    #if 1:
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
            webbrowser.open("https://www.youtube.com/")
        elif 'open jupyter notebook' in query:
            webbrowser.open("https://www.jupyter.org/")
        elif 'open github' in query:
            webbrowser.open("https://www.github.com/")        
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open gmail' in query:
            webbrowser.open('https://mail.google.com/mail/u/0/?ogbl#inbox')
        elif 'open facebook' in query:
            webbrowser.open("https://www.facebook.com/")
        elif 'play some music' in query:
            music_dir = 'C:\\Users\\Prakash Anand\\Downloads\\music'
            songs=os.listdir(music_dir)
            
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%d %B, %Y")
            print(strTime)
            str1Time=datetime.datetime.now().strftime("%H:%M:%S")
            print(str1Time)
            speak(f"Sir,Today  is {strTime}")
            speak(f"And the time Today  is {str1Time}")
        elif 'open sublime' in query:
            codepath='C:\\Program Files\\Sublime Text 3\\sublime_text.exe'
            os.startfile(codepath)
        elif 'send email to prakash' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="ppa58514@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Incorrect email id, I am able to send this mail.")
        elif 'send email to sudo' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="deepesh.97kumar@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Incorrect email id, I am able to send this mail.")
        elif 'send email to vikas ji' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="er.vikashs4@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Incorrect email id, I am able to send this mail.")
        elif 'send email to abhishek ji' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="abhiit9831@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Incorrect email id, I am able to send this mail.")          
        elif 'goodbye' in query:
            speak(f"Good bye {n}")
            speak("See you soon")
            quit()
        elif 'thanks jarvis' in query:
            speak(f"Good bye {n}")
            speak("See you soon")
            quit()    
                      

                
            
            
            

            
            
            

            	
