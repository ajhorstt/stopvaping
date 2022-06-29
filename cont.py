from tkinter import *
# Created on 20/6
def contactus():
    window = Tk()
    window.title("Contact us")
    window.geometry("800x500+250+200")

    cont = Label(window, text="Where to contact us", font=("Helvetica", 20, 'bold'), fg='black')
    cont.pack()

    body1 = Label(window, text="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.", font=("Helvetica", 14), fg='black', padx=50, pady=25)
    body1.pack()

    body2 = Label(window, text="A diam sollicitudin tempor id eu nisl nunc mi. Curabitur gravida arcu ac tortor dignissim convallis.", font=("Helvetica", 14), fg='black')
    body2.pack()

    body3 = Label(window, text="Non blandit massa enim nec dui. Molestie ac feugiat sed lectus vestibulum mattis ullamcorper velit.", font=("Helvetica", 14), fg='black', pady=25)
    body3.pack()

    leftframe = Label(window, width=5, height=500, fg='black', bg='black')
    leftframe.place(x=0, y=0)

    rightframe = Label(window, width=5, height=500, fg='black', bg='black')
    rightframe.place(x=750, y=0)
    # All up to here is 20/6

    window.mainloop()