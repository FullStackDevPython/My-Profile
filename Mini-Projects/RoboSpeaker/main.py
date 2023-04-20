import os 
import win32com.client as wincom

if __name__ == '__main__':
    speak= wincom.Dispatch("SAPI.SpVoice")
    print("Welcome to RoboSpeaker 1.1. Created by Shashank")
    while True:
        x= input("Enter what you want me to speak: ")
        if x == "q":
            #Say Command for Mac Users
            # os.system("Say bye bye friend")
            print(speak.Speak("bye bye friend take care"))
            
            break
        #Say Command for Mac Users
        # command = f"say {x}"
        # os.system(command)
        print(speak.Speak(x))
