from tkinter import *

from PIL import ImageTk, Image


def mainprog():
    # ADD ALL THE OTHER STUFF!!
    '''def createinst():
        root.destroy()
        root1 = Tk()
        root1.title("INSTRUCTIONS")
        root1.geometry("800x500+250+200")
        inst = Label(root1, text='instructions', width=800, height=500, bg='black')
        inst.place(x=0, y=0)
        inst.pack()
        root1.mainloop()'''

    def getinst():
        root.destroy()
        from instructions import inst
        inst()

    def createbig():
        root.destroy()
        from bigpicture import big
        big()

    def createcons():
        root.destroy()
        from consequences import cons
        cons()

    def createcont():
        root.destroy()
        from cont import contactus
        contactus()

# The functions above are used as commands to open the various windows

    root = Tk()
    root.title("...")  # Window title
    root.geometry("800x500+250+200") # Set as a specific size (done across all windows)
    root.resizable(False, False)
    # Setting up the window with tk, the root title and the geometry commands. Window cannot be resizable
    titlelabel = Label(root, text="Bruh i need to find a title for this", font=("Helvetica", 20, 'bold'), fg='white',
                       bg='black')
    titlelabel.pack()  # This is the text that goes up the top

    instructions = Button(root, text="How to use this app", bg='black', height=2, command=getinst)
    instructions.place(x=650, y=0)

    button1 = Button(root, text="The big picture", height=3, width=20, command=createbig)
    button1.config(bg='#000000', fg='blue')
    button1.place(x=80, y=50)
    # , command=getridofwindowlol()

    button2 = Button(root, text="What are the consequences?", height=3, width=22, fg='blue', command=createcons)
    button2.place(x=300, y=50)

    button4 = Button(root, text="Contact Us!", height=3, width=20, fg='blue', command=createcont)
    button4.place(x=520, y=50)
    # All buttons have been placed/made, but STILL need to figure out button commands ffs

    frame = Frame(root, width=50, height=50)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.55)

    # Opening image that is on the main window, resized to fit how I wanted it to fit
    img = Image.open("img/vaping-bans (1).webp")
    resize_img = img.resize((375, 275))
    image = ImageTk.PhotoImage(resize_img)
    label = Label(frame, image=image)
    label.pack()

    l1 = Label(root, text=
    "Vaping is a serious issue as many of us know But are people really informed about how much they should know?")
    l1.pack()
    l1.place(x=60, y=425)

    l2 = Label(root, text=
    "This app gives you information about what you need to know and how to keep yourself + others out of danger.")
    l2.pack()
    l2.place(x=60, y=450)

    results = open("testtext.txt", "a")
    results.write("Yeahhh\n")
    root.mainloop()


mainprog()
