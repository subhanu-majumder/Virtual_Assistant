from os import *
import os

system("title FRIDAY")
import datetime
import random
import smtplib
import sys
import time
import webbrowser
from sympy import *

import keyboard
import pyttsx3
import wikipedia
from googlesearch import search
from tqdm import tqdm
from translate import *
import speech_recognition as sr

r = sr.Recognizer()

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("rate", 178)
engine.setProperty("voice", voices[1].id)

ques = (
    "What else can I do for you Sir?",
    "Anything else Sir?",
    "What else to do?",
    "How can I help you?",
    "What else do you need?",
)


def speak(audio):
    print(audio)
    time.sleep(0.5)
    # engine.say(audio)
    # engine.runAndWait()


def load_bar():
    for val in tqdm(range(100), desc="Loading", ascii=False, ncols=75):
        time.sleep(0.03)


def take_command():
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            query = r.recognize_google(audio, language="en-in")
            speak(query)
        except Exception as e:
            # print(e)
            speak("Couldn't recognise command...")
            speak("Please say that again...")
            return take_command()
        return query


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
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("neel.majumder005@gmail.com", "suvajit.majumder")
    server.sendmail("neel.majumder005@gmail.com", receiver_mail, message)
    server.close()


def search_wiki(subject):
    speak("Searching Wikipedia...")
    subject = subject.replace("wikipedia", "")
    results = wikipedia.summary(subject, sentences=2)
    ind = results.index("(")
    ind2 = results.index(")")
    ns = results[ind : ind2 + 1]
    results = results.replace(ns, "")
    results = results.replace(")", "")
    speak("According to Wikipedia")
    speak(results)


def translate():
    speak("To which language you want to translate?")
    lang = take_command()
    translator = Translator(to_lang=lang)
    speak("What should I translate?")
    text = take_command()
    translation = "The translated text is " + translator.translate(text)
    speak(translation)


if __name__ == "__main__":
    wishMe()
    while True:
        time.sleep(1)
        query = take_command().lower()
        speak("Recognizing command...")
        # Logic for executing tasks based on query
        try:
            if "wikipedia" in query:
                search_wiki(query)

            elif "open youtube" == query:
                webbrowser.open_new("https://www.youtube.com/")

            elif "open onedrive" == query:
                webbrowser.open_new(
                    "https://theheritageschooll-my.sharepoint.com/personal/suvajit_majumder_theheritageschool_ind_in/_layouts/15/onedrive.aspx"
                )

            elif "open hoichoi" in query:
                webbrowser.open_new("https://www.hoichoi.tv/home")

            elif "open hotstar" in query:
                webbrowser.open_new("https://www.hotstar.com/in")

            elif "open google" == query:
                webbrowser.open_new("https://www.google.com")

            elif "open classroom" in query:
                webbrowser.open_new("https://classroom.google.com/u/1/h")

            elif "open mail" in query:
                webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")

            elif "open intellij" == query:
                os.startfile("idea64")

            elif ".com" in query:
                index = query.index(".com") + 3
                index2 = 0
                for i in range(index, -1, -1):
                    if query[i] == " ":
                        index2 = i + 1
                        break
                query = "www." + query[index2 : index + 1]
                webbrowser.open_new(query)

            elif "play music" in query:
                codepath = "C://Users//91916//AppData//Roaming//Spotify//Spotify.exe"
                os.startfile(codepath)
                time.sleep(4)
                keyboard.press_and_release("space")

            elif "translate" in query:
                translate()

            elif "create file" in query:
                directory = take_command("Enter the directory :: ")
                save_path = "C://Users//91916//" + directory
                name_of_file = take_command("What is the full name of the file :: ")
                completeName = os.path.join(save_path, name_of_file)
                file1 = open(completeName, "w")
                file1.close()

            elif "open file" in query:
                directory = take_command("Enter the directory :: ")
                save_path = "C://Users//91916//" + directory
                name_of_file = take_command("What is the full name of the file :: ")
                full_path = save_path + "//" + name_of_file
                os.startfile(full_path)

            elif "delete file" in query:
                directory = take_command("Enter the directory :: ")
                save_path = "C://Users//91916//" + directory
                name_of_file = take_command("What is the full name of the file :: ")
                full_path = save_path + "//" + name_of_file
                os.remove(full_path)

            elif "time" in query:
                hours = datetime.datetime.now().hour
                minutes = datetime.datetime.now().minute
                ns = ""
                if hours <= 12:
                    ns += str(hours) + ":" + str(minutes) + " a.m."
                    pyttsx3.init().say(
                        "The time is " + str(hours) + str(minutes) + "am"
                    )
                else:
                    hours -= 12
                    ns += str(hours) + ":" + str(minutes) + " p.m."
                    pyttsx3.init().say(
                        "The time is " + str(hours) + str(minutes) + "pm"
                    )
                print(ns)

            elif "send mail" in query:
                try:
                    speak("To whom should I send")
                    to = take_command()
                    speak("What should I say?")
                    content = take_command()
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Sir, couldn't send email...")

            elif "print file" in query:
                directory = take_command("Enter the directory :: ")
                save_path = "C://Users//91916//" + directory
                name_of_file = take_command("What is the full name of the file :: ")
                full_path = save_path + "//" + name_of_file
                os.startfile(full_path, "print")

            elif "open" in query:
                query = query.replace("open ", "")
                os.startfile(query)

            elif "quit" in query:
                speak("Ok Sir, All Systems shutting down...")
                load_bar()
                speak("All systems successfully terminated...")
                time.sleep(1)
                speak("Exiting...")
                sys.exit("")

            elif "search" in query:
                query = query.replace("search", "")
                speak("I found these on the internet")
                for j in search(query, tld="co.in", num=2, stop=2, pause=2):
                    webbrowser.open_new(j)
            else:
                query = query.replace("search", "")
                speak("I found these on the internet")
                for j in search(query, tld="co.in", num=2, stop=2, pause=2):
                    webbrowser.open_new(j)
        except Exception as e:
            speak("I didn't get that...")
            speak("Plese tell me what you want...")
            continue

        i = random.randint(0, len(ques) - 1)
        speak(ques[i])
