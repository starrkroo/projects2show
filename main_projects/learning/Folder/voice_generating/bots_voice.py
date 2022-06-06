import pyttsx3

def speak(what):
	print(what)
	speak_engine.say(what)
	speak_engine.runAndWait()
	speak_engine.stop()


speak_engine = pyttsx3.init()
speak_engine.setProperty('voices', speak_engine.getProperty('voices')[1].id)

speak('hello world')