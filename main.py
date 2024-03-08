import os
import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    
    print("Welcome to Your Pc Speak")
    
    while True:
        x = input("Enter what you want your device to speak: ")
        
        if x == "q":
            engine.say("See you again")
            engine.runAndWait()
            break
        
        engine.say(x)
        engine.runAndWait()
