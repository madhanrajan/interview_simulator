import pyttsx3
import random

def say(txt):
    engine = pyttsx3.init()
    engine.say(txt)
    engine.runAndWait()

with open('ques2.txt','r') as f:
    output = f.read().split('\n')
    say(random.choice(output))



