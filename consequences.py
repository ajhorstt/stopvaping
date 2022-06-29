from tkinter import *
# Created on 22/6
def cons():
    window = Tk()
    window.title("The consequences")
    window.geometry("800x500+250+200")

    cons = Label(window, text="What are the consequences of vaping?", font=("Helvetica", 20, 'bold'), fg='black')
    cons.pack()

    button1 = Button(window, text="The big picture", height=3, width=20)
    button1.config(bg='#000000', fg='blue')
    button1.place(x=80, y=50)
    # , command=getridofwindowlol()

    button2 = Button(window, text="BACK TO MAIN", height=3, width=22, fg='red')
    button2.place(x=300, y=50)

    button4 = Button(window, text="Contact Us!", height=3, width=20, fg='blue')
    button4.place(x=520, y=50)
    # All buttons have been placed/made, but STILL need to figure out button commands ffs

    body1 = Label(window, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.", font=("Helvetica", 14), fg='black', padx=50, pady=25)
    body1.pack()
    body1.place(x=25, y=125)

    body2 = Label(window, text="A diam sollicitudin tempor id eu nisl nunc mi. Curabitur gravida arcu ac tortor dignissim convallis.", font=("Helvetica", 14), fg='black', padx=50)
    body2.pack()
    body2.place(x=25, y=175)

    body3 = Label(window, text="Non blandit massa enim nec dui. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit.", font=("Helvetica", 14), fg='black', padx=50)
    body3.pack()
    body3.place(x=25, y=225)

    leftframe = Label(window, width=5, height=500, fg='black', bg='black')
    leftframe.place(x=0, y=0)

    rightframe = Label(window, width=5, height=500, fg='black', bg='black')
    rightframe.place(x=750, y=0)

    window.mainloop()