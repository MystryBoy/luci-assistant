import os
import webbrowser #pip install webbrowser (for open web pages)
from tkinter import * # pip install tkintert
from tkinter import messagebox
from tkinter import filedialog
import pyttsx3 #  pip install pyttsx3
import re
import speech_recognition as sr #pip install SpeechRecognition #pip install PyAudio
import time #pip install time
import pyautogui #pip install pyautogui (for take screen shot)
from pygame import mixer #pip install pygame (for play sound)
import random #pip install random
import keyboard as key # pip installl keyboard
#----------------------make a window -----------------------------------------------------
window = Tk()
window.geometry("300x160")
window.title("luci assistant 1.0.0 (EN)")
window.iconbitmap(r'Untitled-45.ico')
window.config(bg='#303334')
window.resizable(0,0)
#---------------------------text to speech(pyttsx3) ------------------------
engine = pyttsx3.init()
engine.setProperty('rate' , 120)
voices = engine.getProperty("voices")
engine.setProperty('voices', voices[1].id)
#---------------------------make a txt file---------------------------------------
User_name_new = open("User__name.txt" , "w")
User_name_new.write("")
User_name_new.close()
#--------------------------read user name in txt file---------------------------
User_name = open("User__name.txt" , "r")
#-------------------------make a file for name -----------------------------------
try:
    read_your_name_1 = open("your_name.txt","r")
    read_your_name_1.close()
except:
    os.system(f"echo sir >> your_name.txt")
#------------------------ read name --------------------------------------
read_your_name = open("your_name.txt","r")


engine = pyttsx3.init()
engine.setProperty('rate' , 120)
voices = engine.getProperty("voices")
def questions():
#-----------------------change Icon and title-----------------------------------
    window.title("luci assistant 1.0.0 (EN)")
    window.iconbitmap('Untitled-45.ico')


    luci = question_entry.get()
    luci_1 = name_.get()
    Dir_1 = Directory_entry.get()


    if luci_1 == "":
        name_your = read_your_name.read()
        name_.insert(0,name_your)
        read_your_name.close()
#-------------------------------insert user name in txt file-----------------------
    if Dir_1 == "":#User__name.txt
        os.system("echo %username% >>  User__name.txt")
        user = User_name.read()
        user_len = len(user)
        user___ = user_len - 2
        Directory_entry.delete(0,END)
        Directory_entry.insert(0,f"C:\\Users\\{user[0:user___]}\\Desktop")#C:\YU
        User_name.close()
        os.remove("User__name.txt")

#-------------------------------------search(re)-------------------------------------

    words=("hi","hello","what is my name","bye","restart my pc" , "shut down my pc" ,"shut down my computer",  "spell" ,
    "what is your name","say" ,"write","call me" ,"take a screenshot","how are you" , "what's up",
    "me too" , "i'm ok" ,"i have to go","open a file","open a picture","open a video",
    "nice to meet you" , "i'm happy to see you" ,
    "i love you","")

    

            

    pattern = re.compile(f".?{luci[0:5].lower()}")

    for word in words:
        if re.search(pattern,word):
            search_23=(f"{word}")
            question_entry.delete(0,END)    
            question_entry.insert(0, search_23 ) 


    


#---------------------------speech to text(speec_recogniz)-----------------------------------------------

    if  luci == "":
        window.title("Say something ...")
        window.iconbitmap(r'TALK.ico')
        path_start = r"start.mp3"
        mixer.init()
        mixer.music.load(path_start)
        mixer.music.play()
        answer_entry.delete(0,END)
        try:
            r = sr.Recognizer()
            with sr.Microphone() as sound : 
                voice = r.listen(sound)
                try:
                    question_entry.insert(0, r.recognize_google(voice))
                    questions()
                except:
                    pass
        except:
            mixer.music.stop()
            window.title("luci assistant 1.0.0 (EN)")
            window.iconbitmap('Untitled-45.ico')
            Error_ = messagebox.showwarning("ERROR","Please use a Microphone or check your internt Connection")
        finally:
            window.title("luci assistant 1.0.0 (EN)")
            window.iconbitmap('Untitled-45.ico')
        
            

#----------------------------- word and sentenses you can say-----------------------------

    
    word_1 = ["spell"  , "write"]
     
    for lol_1 in word_1:
        if lol_1 in luci.lower():      
            answer_entry.delete(0,END)
            answer_entry.insert(0,luci[5::])
            engine.say(luci[5::])
            question_entry.delete(0,END)

    if "say" in luci.lower():
        answer_entry.delete(0,END)
        answer_entry.insert(0,luci[5::])
        engine.say(luci[4::])
        question_entry.delete(0,END)


    word_2 = ["hello" , "hey"]

    for lol_2 in word_2:
        if lol_2 in luci.lower():
            answer_entry.delete(0,END)
            answer_entry.insert(0," hello " + name_.get() + " my name is luci how can I help you?")
            engine.say("hello " + name_.get()  + " my name is luci how can I help you?")
            question_entry.delete(0,END)

    if luci[0:2] == "hi".lower():
        answer_entry.delete(0,END)
        answer_entry.insert(0," hello " + name_.get() + " my name is luci how can I help you?")
        engine.say("hello " + name_.get() + " my name is luci how can I help you?")
        question_entry.delete(0,END)
            

    word_3 = ["what is my name" , "whats my name" , "what's my name" ]

    for lol_3 in word_3:
        if lol_3 in luci.lower():
            if "sir" in name_.get():
                answer_entry.delete(0,END)
                answer_entry.insert(0," I don't know what is your name")
                engine.say(" I don't know what is your name")
                question_entry.delete(0,END)
            else:
                answer_entry.delete(0,END)
                answer_entry.insert(0," Your name is " + name_.get() )
                engine.say("Your name is " + name_.get() )
                question_entry.delete(0,END)

    word_4 = ["bye" , "i have to go"]

    for lol_4 in word_4 : 
        if lol_4 in luci.lower():
            answer_entry.delete(0,END)
            answer_entry.insert(0," bye bye " + name_.get() )
            engine.say("bye bye "  + name_.get() )
            question_entry.delete(0,END)
            window.quit()





#-------------------------restart compute(os)--------------------------

    word_5 = [ "restart" , "restarte" ]

    for lol_5 in word_5:
        if lol_5 in luci.lower():
            answer_entry.delete(0,END)
#---------------------------message Box for Restart computer(TK)--------------------------
            B =  messagebox.askyesno("Restart pc" , "are you sure ? ")
            if B == True :
                os.system('shutdown -r')
                answer_entry.insert(0,"your pc will restarted")
                engine.say("your pc will restarted")
                window.quit()

            if B == False :
                question_entry.delete(0,END)
                answer_entry.insert(0,"ok")
                engine.say("ok")

#-------------------------shut down compute(os)--------------------------

    word_6 = ["shutdown" , "shutdowne" , "shut down"]

    for shut in word_6:
        if  shut in luci.lower():
            answer_entry.delete(0,END)
#---------------------------message Box for Restart computer(TK)--------------------------
            s =  messagebox.askyesno("Shut down pc" , "are you sure ? ")
#-----------------------------------------------------------------------------------------
            if s == True :
                os.system('shutdown -s')
                answer_entry.insert(0,"Your PC will shut down")
                engine.say("Your PC will shut down")
                window.quit()

            if s == False :
                question_entry.delete(0,END)
                answer_entry.insert(0,"ok")
                engine.say("ok")

#---------------------------------open a web page (webbbrowser)------------------------------------------------

    webs = ["www.","https",".com",".ir",".org",".html"]

    for w in webs:
        if w in luci.lower():
            answer_entry.insert(0," ok")
            engine.say("ok")
            webbrowser.open_new(luci)
            question_entry.delete(0,END)



#-----------------------------open file(os)-----------------------------------------

    pop = [".mp3" , ".mp4", ".png" , ".lnk" , ".txt" , ".jpg" , ".apk" , ".pdf" , ".ico" , ".exe"]


    for str_vid in pop:
        if str_vid in luci.lower():
            answer_entry.delete(0,END)
            liso = os.listdir(Directory_entry.get())
            for an in liso:
                if an in luci:
                    key.press_and_release("Windows+r")
                    time.sleep(0.5)
                    key.write(f"{Directory_entry.get()}\\{luci}")
                    time.sleep(0.5)
                    key.press("Enter")
                    question_entry.delete(0,END)
                    answer_entry.delete(0,END)
                    answer_entry.insert(0,luci + " opening")
                    engine.say(luci + " opening")
                    question_entry.delete(0,END)
#----------------------------------------------------------------

    pop_1 = ["what is your name" , "what's your name" , "youre"]
    

    for sentences in pop_1:
        if sentences in luci.lower():
            answer_entry.delete(0,END)
            answer_entry.insert(0," My name is luci")
            engine.say("My name is luci")
            question_entry.delete(0,END)


    open_file = ["open a file","open a picture","open a video"]

    for opens in open_file:
        if opens in luci.lower():
            answer_entry.delete(0,END)
            answer_entry.insert(0," ok , Enter your file name here")
            engine.say(" ok , Enter your file name here")
            question_entry.delete(0,END)

    screen_shot_say = ["take a screenshot" , "screenshote"]

    for word_screen in screen_shot_say:
        if word_screen in luci.lower():
            window.iconify()
            answer_entry.insert(0,"ok here we go")
            engine.say("ok here we go")
            path = r"shutter2_sfx.mp3"
            mixer.init()
            mixer.music.load(path)
            mixer.music.play()
            time.sleep(1)
            ran = int(random.uniform(1,100000))
            try:
                screen_shot = pyautogui.screenshot(f"{Directory_entry.get()}\\luci screenshots\\screenshot ({ran}).png")
            except:
                os.mkdir(f"{Directory_entry.get()}\\luci screenshots")
                screen_shot = pyautogui.screenshot(f"{Directory_entry.get()}\\luci screenshots\\screenshot ({ran}).png")
            question_entry.delete(0,END)
            key.press_and_release("Windows + r")
            time.sleep(0.5)
            key.write(f"{Directory_entry.get()}\\luci screenshots\\screenshot ({ran}).png")
            time.sleep(0.5)
            key.press("Enter")

#-------------------------------change your name-----------------------------
    if "call me" in luci.lower():    
        question_entry.delete(0,END)
        answer_entry.delete(0,END)
        Pop = messagebox.askyesno("Are you sure ? " , f"would you like I call you {luci[7::]} ? ")
        if Pop == True:
            name_.delete(0,END)
            name_.insert(0,luci[7::])
            answer_entry.insert(0,f"ok {luci[7::]}")
            engine.say(f"ok {luci[7::]}")
            os.system("del your_name.txt /q")
            os.system(f"echo {luci[7::]} >> your_name.txt")
        if Pop == False :
            answer_entry.insert(0,f"ok")
            engine.say(f"ok")

    if "my name is" in luci.lower():    
        question_entry.delete(0,END)
        answer_entry.delete(0,END)
        Pop = messagebox.askyesno("Are you sure ? " , f"would you like I call you {luci[10::]} ? ")
        if Pop == True:
            name_.delete(0,END)
            name_.insert(0,luci[10::])
            answer_entry.insert(0,f"ok {luci[10::]}")
            engine.say(f"ok {luci[10::]}")
            os.system("del your_name.txt /q")
            os.system(f"echo {luci[10::]} >> your_name.txt")
        if Pop == False :
            answer_entry.insert(0,f"ok")
            engine.say(f"ok")



    if "change my name to" in luci.lower():    
        question_entry.delete(0,END)
        answer_entry.delete(0,END)
        Pop = messagebox.askyesno("Are you sure ? " , f"would you like I call you {luci[17::]} ? ")
        if Pop == True:
            name_.delete(0,END)
            name_.insert(0,luci[17::])
            answer_entry.insert(0,f"ok {luci[17::]}")
            engine.say(f"ok {luci[17::]}")
            os.system("del your_name.txt /q")
            os.system(f"echo {luci[17::]} >> your_name.txt")
        if Pop == False :
            answer_entry.insert(0,f"ok")
            engine.say(f"ok")




    how = ["how are you" , "whats up" , "what's up"]
    for h in how:
        if h in luci.lower():
            answer_entry.delete(0,END)
            answer_entry.insert(0," I'm ok How about you ? ")
            engine.say(" I'm ok How about you ? ")
            question_entry.delete(0,END)

    ho = ["me too" , "im ok" , "i'm ok"]
    for im in ho:
        if im in luci.lower():
            answer_entry.delete(0,END)
            answer_entry.insert(0," good ")
            engine.say(" good ")
            question_entry.delete(0,END)


    Dire = ["directory"]
    for Di in Dire:
        if Di in luci.lower():
            answer_entry.delete(0,END)
            answer_entry.insert(0," ok choice a Directory")
            path = filedialog.askdirectory(initialdir="/", title="Choice a directory")
            answer_entry.delete(0,END)
            Directory_entry.delete(0,END)
            Directory_entry.insert(0,path)
            answer_entry.insert(0,f"ok directory changed to {path}")
            engine.say(f"ok directory changed to {path}")
            question_entry.delete(0,END)

    me_to = ["nice to meet you" , "i'm happy to see you" , "im happy to see you" , "i love you"
               , "i like you" , "you're my favorite friend" , "you are my favorite friend"]
    for this in me_to:
        if this in luci.lower():
            answer_entry.delete(0,END)
            answer_entry.insert(0,f"me to {name_.get()}")
            engine.say(f"me to {name_.get()}")
            question_entry.delete(0,END)

    jokes = ["What did the lava say to his girlfriend? I lava you" , "What is a room with no walls? A mushroom."
    , "What is brown, hairy and wears sunglasses? A coconut on vacation." , "How do you stop an astronaut's baby from crying? You rocket."]

    if "joke" in luci.lower():
        answer_entry.delete(0,END)
        answer_entry.insert(0,"ok")
        engine.say("ok")
        answer_entry.delete(0,END)
        JOKE = random.choice(jokes)
        answer_entry.insert(0,JOKE)
        engine.say(JOKE)
        question_entry.delete(0,END)

    if "open" in luci.lower():
        answer_entry.delete(0,END)
        key.press_and_release("Windows+r")
        time.sleep(0.5)
        key.write(f"{luci[4::]}")
        time.sleep(0.5)
        key.press("Enter")
        answer_entry.insert(0,f"ok {luci[4::]} opening")
        engine.say(f"ok {luci[4::]} opening")
        question_entry.delete(0,END)


    engine.runAndWait()

#-------------------------open google(window)----------------------------
def goog():
    search_1 = "www.google.com"
    webbrowser.open_new(search_1)  
#---------------------------------About(top1)---------------------------------
def Ab():
    github = "www.github.com/MystryBoy"
    webbrowser.open_new(github) 
#-------------------------------------------quite(window)-------------------------------
def qui ():
    window.quit()


#----------------------------------------you can say------------------------------------
def hello():
    question_entry.delete(0,END)
    cut_ = question_entry.insert(0," hello")
    answer_entry.delete(0,END)

def bye():
    question_entry.delete(0,END)
    cut_ = question_entry.insert(0," bye")
    answer_entry.delete(0,END)

def what():
    question_entry.delete(0,END)
    cut_ = question_entry.insert(0," what is my name")
    answer_entry.delete(0,END)

def shut():
    question_entry.delete(0,END)
    cut_ = question_entry.insert(0," shut down my pc")
    answer_entry.delete(0,END)

def res():
    question_entry.delete(0,END)
    cut_ = question_entry.insert(0," restart my pc")
    answer_entry.delete(0,END)

def open_():
    question_entry.delete(0,END)
    cut_ = question_entry.insert(0," open a file")
    answer_entry.delete(0,END)

def screen():
    question_entry.delete(0,END)
    cut_ = question_entry.insert(0," Take a screenshot")
    answer_entry.delete(0,END)


def cleare():
    question_entry.delete(0,END)
    answer_entry.delete(0,END)

def unmute():
    Button_unmute.grid_remove()
    volume = engine.getProperty('volume')
    engine.setProperty('volume',0.9)

def mute():
    volume = engine.getProperty('volume')
    engine.setProperty('volume',0)
    Button_unmute.grid(column=1 , row=2 , padx=5 ,pady= 5)
#---------------------------(make Button , entry and ...)----------------------------
button_delete = Button(window,text="Cleare",bg='#5f5e5e' , fg='white' , width='12', command=cleare )
question_entry=Entry(window,bg='#5f5e5e',fg='white',width=23)
answer_entry=Entry(window,bg='#5f5e5e',fg='white',width=23)
button_question=Button(window,text="enter",bg='#5f5e5e',fg='white',width='12',command=questions)
name_=Entry(window,bg='#5f5e5e',fg='white',width=23)
Directory_entry=Entry(window)
Button_mute = Button(window ,text="Mute",bg='#5f5e5e' , fg='white' , width='12' , command=mute)
Button_unmute = Button(window ,text="Unmute",bg='#5f5e5e' , fg='white' , width='12' , command=unmute)
#--------------------------------Menu(you can say)------------------------------------
menubar = Menu(window)
say_menu = Menu(menubar , tearoff= 0)
menubar.add_cascade(label="you can say" , menu=say_menu)
menubar.add_command(label="google" , command = goog)
menubar.add_command(label="github" , command = Ab )
menubar.add_command(label="quite" , command = qui)
say_menu.add_command(label="hello" , command= hello )
say_menu.add_command(label="bye" , command = bye)
say_menu.add_command(label="what is my name" , command= what)
say_menu.add_command(label="shut down my pc" , command= shut)
say_menu.add_command(label="restart my pc " , command = res)
say_menu.add_command(label="open a file" , command=open_)
say_menu.add_command(label="Take a screenshot" , command=screen)




question_entry.grid(column=0 , row=0 , pady=10 , padx=10)
button_question.grid(column=1 , row=0 , padx=5 , pady=5)
answer_entry.grid(column=0 , row=1 , pady=5 , padx=5)
button_delete.grid(column=1 , row=1 , padx=5 ,pady= 5)
Button_mute.grid(column=1 , row=2 , padx=5 ,pady= 5)
window .config(menu=menubar)

window.mainloop()

