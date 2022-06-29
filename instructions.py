from tkinter import *
    # Created on 20/6

def inst():
    def getmain():
        window.destroy()
        from main import mainprog
        mainprog()

    window = Tk()
    window.title("Instructions")
    window.geometry("800x500+250+200")

    instructions = Label(window, text="How to use this app:", font=("Helvetica", 20, 'bold'), fg='black')
    instructions.pack()


    button1 = Button(window, text="The big picture", height=3, width=20)
    button1.config(bg='#000000', fg='blue')
    button1.place(x=80, y=50)
    # , command=getridofwindowlol()

    button2 = Button(window, text="What are the consequences?", height=3, width=22, fg='blue')
    button2.place(x=300, y=50)

    button4 = Button(window, text="Contact Us!", height=3, width=20, fg='blue')
    button4.place(x=520, y=50)

    button5 = Button(window, text="back to main :))", height=1, width=15, fg='red', command=getmain)
    button5.place(x=120, y=10)

    body1 = Label(window, text="This app is very easy to use.", font=("Helvetica", 14), fg='black', padx=50)
    body1.pack()
    body1.place(x=25, y=125)

    body2 = Label(window, text="All you need to do is click the button assigned to what you want to know about vaping.",
                  font=("Helvetica", 14), fg='black', padx=50)
    body2.pack()
    body2.place(x=25, y=160)

    body3 = Label(window,
                  text="There are three main buttons: "
                       "one gives you a wider view about vaping (why this is a problem)",
                  font=("Helvetica", 14), fg='black', padx=50)
    body3.pack()
    body3.place(x=25, y=195)

    body4 = Label(window,
                  text="Another one shows you the consequences of vaping, "
                       "and the other one shows you a google form which can be used to contact us.",
                  font=("Helvetica", 14), fg='black', padx=50)
    body4.pack()
    body4.place(x=25, y=275)

    leftframe = Label(window, width=5, height=500, fg='black', bg='black')
    leftframe.place(x=0, y=0)

    rightframe = Label(window, width=5, height=500, fg='black', bg='black')
    rightframe.place(x=750, y=0)
    # Basics done on 20/6
    # Buttons added and text reconfigured on 27/6

    window.mainloop()