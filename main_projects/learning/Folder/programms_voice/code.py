#!/usr/bin/env python3

import pyttsx3
speak_engine = pyttsx3.init()

voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[4].id)


def speak(what):
	print( what )
	speak_engine.say( what )
	speak_engine.runAndWait()
	speak_engine.stop()

speak('hellow orl')