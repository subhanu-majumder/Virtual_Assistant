import datetime
import os
import random
import smtplib
import sys
import time
import webbrowser

import keyboard
import pyttsx3
import wikipedia
from googlesearch import search
from tqdm import tqdm
from translate import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('rate', 178)
engine.setProperty('voice', voices[1].id)

ques = ("What else can I do for you Sir?", "Anything else Sir?",
        "What else to do?", "How can I help you?", "What else do you need?")


def load_bar():
    for val in tqdm(range(100), desc="Loading", ascii=False, ncols=75):
        time.sleep(0.03)


def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hours = int(datetime.datetime.now().hour)
    if 0 <= hours < 12:
        speak("Good Morning Sir!")

    elif 12 <= hours < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")
    speak("All Systems initiating...")
    load_bar()
    speak("All systems successfully initiated...")
    speak("What can I do for you sir?")


def sendEmail(receiver_mail, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_mail@gmail.com', 'your_password')
    server.sendmail('your_mail@gmail.com', receiver_mail, message)
    server.close()


def search_wiki(subject):
    speak('Searching Wikipedia...')
    subject = subject.replace("wikipedia", '')
    results = wikipedia.summary(subject, sentences=2)
    ind = results.index('(')
    ind2 = results.index(')')
    ns = results[ind:ind2 + 1]
    results = results.replace(ns, '')
    results = results.replace(')', '')
    speak("According to Wikipedia")
    speak(results)


def translate():
    speak("To which language you want to translate?")
    lang = input()
    translator = Translator(to_lang=lang)
    speak("What should I translate?")
    text = input()
    translation = translator.translate(text)
    speak(translation)


if __name__ == "__main__":
    wishMe()
    while True:
        time.sleep(1)
        query = input().lower()
        speak("Recognizing command...")
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            search_wiki(query)

        elif 'open youtube' == query:
            webbrowser.open_new("https://www.youtube.com/")
        
        elif 'open google' == query:
            webbrowser.open_new("google.com")

        elif 'open intellij' == query:
            os.startfile("path to intellij")

        elif '.com' in query:
            index = query.index('.com') + 3
            index2 = 0
            for i in range(index, -1, -1):
                if query[i] == ' ':
                    index2 = i + 1
                    break
            query = "www." + query[index2:index + 1]
            webbrowser.open_new(query)

        elif 'play music' in query:
            codepath = "path to spotify"
            os.startfile(codepath)
            time.sleep(4)
            keyboard.press_and_release('space')

        elif 'open' in query:
            query = query.replace("open ", '')
            os.startfile(query)

        elif 'translate' in query:
            translate()

        elif 'create file' in query:
            directory = input("Enter the directory :: ")
            save_path = "C://Users//<name>//" + directory
            name_of_file = input("What is the full name of the file :: ")
            completeName = os.path.join(save_path, name_of_file)
            file1 = open(completeName, "w")
            file1.close()

        elif 'open file' in query:
            directory = input("Enter the directory :: ")
            save_path = "C://Users//<name>//" + directory
            name_of_file = input("What is the full name of the file :: ")
            full_path = save_path + "//" + name_of_file
            os.startfile(full_path)

        elif 'open folder' in query:
            directory = input("Enter the directory :: ")
            if "c://" not in directory:
                directory = "c://"+directory
            os.startfile(directory)

        elif 'delete file' in query:
            directory = input("Enter the directory :: ")
            save_path = "C://Users//<name>//" + directory
            name_of_file = input("What is the full name of the file :: ")
            full_path = save_path + "//" + name_of_file
            os.remove(full_path)

        elif 'time' in query:
            hour = datetime.datetime.now().hour
            Time = ''
            Minute = datetime.datetime.now().minute
            if hour <= 12:
                Time = (str(hour - 12) + ":" + str(Minute) + "a.m.")
                speak(Time)
            elif 12 < hour <= 24:
                if hour == 24:
                    Time = (str(12) + ":" + str(Minute) + " p.m.")
                else:
                    Time = (str(hour - 12) + ":" + str(Minute) + " p.m.")
                speak(Time)

        elif 'send mail' in query:
            try:
                speak("To whom should I send")
                to = input()
                speak("What should I say?")
                content = input()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, couldn't send email...")

        elif 'print file' in query:
            directory = input("Enter the directory :: ")
            save_path = "C://Users//<name>//" + directory
            name_of_file = input("What is the full name of the file :: ")
            full_path = save_path + "//" + name_of_file
            os.startfile(full_path, "print")

        elif 'quit' in query:
            speak("Ok Sir, All Systems shutting down...")
            load_bar()
            speak("All systems successfully terminated...")
            time.sleep(1)
            speak("Exiting...")
            sys.exit('')

        elif 'search ' in query:
            query = query.replace('search', '')
            for j in search(query, tld="co.in", num=2, stop=2, pause=2):
                webbrowser.open_new(j)
        i = random.randint(0, 4)
        speak(ques[i])
