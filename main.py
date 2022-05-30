from tkinter import *

import tk as tk
from PIL import ImageTk, Image


def mainframe1():
    bigframe.forget()
    contframe.forget()
    consframe.forget()
    instframe.forget()
    quitmain = Button(mainframe, text="Quit", command=getridofwindowlol())
    quitmain.grid(column=0, row=1, pady=10, sticky=N)


def instframe1():
    bigframe.forget()
    mainframe.forget()
    consframe.forget()
    contframe.forget()
    quitinst = Button(instframe, text="Quit", command=getridofwindowlol())
    quitinst.grid(column=0, row=1, pady=10, sticky=N)


def bigframe1():
    contframe.forget()
    mainframe.forget()
    consframe.forget()
    instframe.forget()
    quitbig = Button(bigframe, text="Quit", command=getridofwindowlol())
    quitbig.grid(column=0, row=1, pady=10, sticky=N)


def consframe1():
    bigframe.forget()
    instframe.forget()
    mainframe.forget()
    contframe.forget()
    quitcons = Button(consframe, text="Quit", command=getridofwindowlol())
    quitcons.grid(column=0, row=1, pady=10, sticky=N)


def contframe1():
    bigframe.forget()
    mainframe.forget()
    consframe.forget()
    instframe.forget()
    quitcont = Button(contframe, text="Quit", command=getridofwindowlol())
    quitcont.grid(column=0, row=1, pady=10, sticky=N)



def getridofwindowlol():
    root.destroy()


def instruction():
    print("yeah")


root = Tk()
root.title("...")
root.geometry("800x500+250+200")
root.resizable(False, False)

titlelabel = Label(root, text="Bruh i need to find a title for this", font=("Helvetica", 20, 'bold'), fg='black')
titlelabel.pack()

#loc_label = Label(root, text="yeah")
#loc_label.pack()

#search_area = Entry(root, justify='center', width=20, font=("Helvetica", 15))
#search_area.place(x=300, y=50)
#search_area.focus()

#search_button = Button(root, bg='black', text="🔍︎", command=location())
#search_button.place(x=500, y=50)

mainframe = Frame(root, width=800, height=500)
#mainframe.grid(column=0, row=0)

instframe = Frame(root, width=800, height=500)
#instframe.grid(column=0, row=0)

bigframe = Frame(root, width=800, height=500)
#bigframe.grid(column=0, row=0)

consframe = Frame(root, width=800, height=500)

contframe = Frame(root, width=800, height=500)

instructions = Button(root, text="How to use this app", bg='black', height=2, command=instruction())
instructions.place(x=650, y=0)

button1 = Button(root, text="The big picture", height=3, width=20)
button1.config(bg='#000000', fg='blue')
button1.place(x=80, y=50)
#, command=getridofwindowlol()


button2 = Button(root, text="What are the consequences?", height=3, width=22, fg='blue')
button2.place(x=300, y=50)

button4 = Button(root, text="Contact Us!", height=3, width=20, fg='blue')
button4.place(x=520, y=50)

frame = Frame(root, width=50, height=50)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.6)

img = Image.open("img/vaping-bans (1).webp")
resize_img = img.resize((375, 275))
image = ImageTk.PhotoImage(resize_img)
label = Label(frame, image=image)
label.pack()


root.mainloop()
