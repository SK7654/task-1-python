import pyttsx3
import os
# pyttsx3.speak("welcome to my tools")


print(format('--Welcome to my tools --', '^90'))
pyttsx3.speak("wellcome to my  Tech Support")
print("""HELLO USER  I CAN HELP YOU TO RUN THE OS BASE PROGRAM""")
pyttsx3.speak("HELLO USER  I CAN HELP YOU TO RUN THE OS BASE PROGRAM")
print("1.RUN chrome")
pyttsx3.speak("RUN chrome")
print("2.RUN notepad")
pyttsx3.speak("RUN notepad")
print("3.RUN wmplayer")
pyttsx3.speak("RUN wmplayer")
print("4.RUN notepad++")
pyttsx3.speak("RUN notepad++")
print("5.RUN python") 
pyttsx3.speak("RUN python ")
print("6.RUN vlc player")
pyttsx3.speak("RUN vlc")


while True :
     print("chat with me with your requirement : " , end='')
     p = input()
    # print(p)
    # os.system(p)
   
     if ("run" in p) and ("chrome" in p):
       os.system("chrome")
     elif ( ("run" in p ) or ("execute" in p)) and (("notepad" in p) or ("editor" in p)):
       os.system("notepad")
     elif("run" in p ) and ("player" in p) and ("media" in p):
       os.system("wmplayer")
     elif(("run" in p ) or (" execute" in p)) and (("notepad++" in p) or ("editor++" in p)):
       os.system("notepad++")   
     elif (("python" in p) or ("Python" in p) or ("PYTHON" in p)):
       os.system("python") 
     elif (("VLC PLAYER" in p) or ("VLC MEDIA PLAYER" in p) or ("vlc media player" in p)or("Vlc Media Player")or("vlc player" in p)or("vlc" in p)):
       os.system("vlc")
     elif ( "exit" in p) or ("quit" in p):
       break
     else:
       print("dont support")