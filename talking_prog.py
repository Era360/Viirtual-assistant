import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

class talking:
    def talk(text):
        engine.say(text)
        engine.runAndWait()

