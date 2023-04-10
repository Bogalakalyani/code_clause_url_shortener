import pyshorteners
from tkinter import *
import clipboard

root = Tk()
root.title("URL Shortener")
root.geometry("400x300")
myLabel = Label(root,text= "URL Shortener",font=('Helvetica', 15))
e = Entry(root,width = 50,fg = "blue",borderwidth =5)

def short_url():
    try:
        user_input = e.get()
        s = pyshorteners.Shortener()
        output = s.tinyurl.short(user_input)
        myLabel = Label(root,text = output,width = 50,borderwidth = 5,fg = "blue")
        myLabel.pack()
        def copy_url():
            clipboard.copy(output)
            myLabel = Label(root,text = "successfully copied to clipboard.",width = 50,borderwidth = 5,fg = "blue")
            myLabel.pack()
        myButton2 = Button(root,text = "Click me! if you want to copy url to your clipboard",command = copy_url)
        myButton2.pack()

    except pyshorteners.exceptions.ShorteningErrorException:
        message = "Error! while creating the tiny url"
        myLabel = Label(root,text = message,width = 50,borderwidth = 5,fg = "blue")
        myLabel.pack()
        

myButton = Button(root,text = "short the URL",command = short_url)

myLabel.pack()
e.pack()
myButton.pack()
root.mainloop()


