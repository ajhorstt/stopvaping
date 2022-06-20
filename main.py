from tkinter import *

from PIL import ImageTk, Image


def getridofwindowlol():
    root.destroy()


def createmain():
    main = Label(root, text='mainframe', width=800, height=500)
    main.place(x=0, y=0)
    main.pack()


# Still trying to figure this out
def createinst():
    inst = Label(root, text='instructions', width=800, height=500, bg='black')
    inst.place(x=0, y=0)
    inst.pack()


def createbig():
    big = Label(root, text='big ', width=800, height=500, bg='yellow')
    big.place(x=0, y=0)
    big.pack()


def createcons():
    cons = Label(root, text='consequences', width=800, height=500, bg='blue')
    cons.place(x=0, y=0)
    cons.pack()


def createcont():
    cont = Label(root, text='contactus', width=800, height=500, bg='red')
    cont.place(x=0, y=0)
    cont.pack()


root = Tk()
root.title("...")  # Window title
root.geometry("800x500+250+200")
root.resizable(False, False)
# Setting up the window with tk, the root title and the geometry commands. Window cannot be resizable
titlelabel = Label(root, text="Bruh i need to find a title for this", font=("Helvetica", 20, 'bold'), fg='black')
titlelabel.pack()  # This is the text that goes up the top

# loc_label = Label(root, text="yeah")
# loc_label.pack()

# search_area = Entry(root, justify='center', width=20, font=("Helvetica", 15))
# search_area.place(x=300, y=50)
# search_area.focus()

# search_button = Button(root, bg='black', text="🔍︎", command=location())
# search_button.place(x=500, y=50)

mainframe = Frame(root, width=800, height=500)

instructions = Button(root, text="How to use this app", bg='black', height=2, command=createinst())
instructions.place(x=650, y=0)

button1 = Button(root, text="The big picture", height=3, width=20, command=createbig())
button1.config(bg='#000000', fg='blue')
button1.place(x=80, y=50)
# , command=getridofwindowlol()


button2 = Button(root, text="What are the consequences?", height=3, width=22, fg='blue', command=createcons())
button2.place(x=300, y=50)

button4 = Button(root, text="Contact Us!", height=3, width=20, fg='blue', command=createcont())
button4.place(x=520, y=50)
# All buttons have been placed/made, but STILL need to figure out button commands ffs

frame = Frame(root, width=50, height=50)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.6)

# Opening image that is on the main window, resized to fit how I wanted it to fit
img = Image.open("img/vaping-bans (1).webp")
resize_img = img.resize((375, 275))
image = ImageTk.PhotoImage(resize_img)
label = Label(frame, image=image)
label.pack()

# mainframe.grid(column=0, row=0)

instframe = Frame(root, width=800, height=500)
# instframe.grid(column=0, row=0)

bigframe = Frame(root, width=800, height=500)
# bigframe.grid(column=0, row=0)

consframe = Frame(root, width=800, height=500)

contframe = Frame(root, width=800, height=500)

createmain()

root.mainloop()
