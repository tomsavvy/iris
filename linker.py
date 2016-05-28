#!/usr/bin/python

import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:

    f=FloatLayout()
    f.add_widget(Button)
    l1= f.add_widget(Label)
    Button.text='Start'
    Button.on_press(l1.self.print("Say something!"))
    audio = r.listen(source)
 

said = r.recognize_google(audio)


# Speech recognition using Google Speech Recognition
try:
    l1.print("You said:   " + said)
except sr.UnknownValueError:
    l1.print("Could not really get you. \n Kindly repeat")
    AppButton():
except sr.RequestError as e:
    l1.print("Could not request results from Google Speech Recognition service; {0}".format(e))
    AppButton():

from jnius import cast
from jnius import autoclass

Iris = autoclass('org.myapp.Iris')

if said[0:4]=="open":
	Iris.open(said[5:])
