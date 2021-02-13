"""
This is a program which runs after the blind presses the button
so as to talk to its device
"""

# After button press program
import datetime
import pyttsx3
import math


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('yes')

# Waits for the users saying
words = str(input('Enter sentence: ')) # here at first am using typing input for test purposes

def run_words(): 
    if 'help' in words:
        talk('You can ask me about this place, look for you something, read for you even calculate for you some math')  

    elif 'calculate this' in words:
        talk('do you need sum, product, difference or quotient? i can even tell you trigonometric functions like cosine,sine and tangent')
        operation = input()
        if 'cosine' and 'sine' and 'tangent' in operation:
            talk('tell me the angle')
        else:
            talk('tell me the two numbers')

        numbers = input()

        list1 = numbers.split()

        a = int(list1[0])
        b = int(list1[-1])
        c = int(list1[0])

        if 'sum' in operation:
            talk('The answer is')
            talk(a + b)
        elif 'difference' in operation:
            talk('The answer is')
            talk(a - b)
        elif 'product' in operation:
            talk('The answer is')
            talk(a * b)
        elif 'quotient' in operation:
            talk('The answer is')
            talk(a / b)
        elif 'cosine' in operation:
            talk('The radian of cosine is'+ c)
            talk(round(math.cos(c), 3))
        elif 'sine' in operation:
            talk('The radian of sine is'+ c)
            talk(round(math.sin(c), 3))
        elif 'tangent' in operation:
            talk('The radian of tangent is'+ c)
            talk(round(math.tan(c), 3))
        else:
            talk('i did not understand your operation, try again when you are ready')
    else:
        talk('i did not understand, but you can ask me anytime')


while True:
    run_words()
    break
