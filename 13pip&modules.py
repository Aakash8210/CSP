import pyjokes
joke=pyjokes.get_joke()
print(joke)
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
import os

directory_path= '/your/directory/path'
contents=os.listdir(directory_path)
for item in contents:
    print(item)
a=31
t=type(a)
print(t)