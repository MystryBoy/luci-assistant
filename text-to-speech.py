import pyttsx3

def spell(text):
    engine = pyttsx3.init()
    engine.setProperty('rate' , 120)
    voices = engine.getProperty("voices")
    engine.say(text)
    engine.runAndWait()

while True:
    txt = input("write a word >>>")
    if txt == "q".lower():
        break
    spell(txt)
