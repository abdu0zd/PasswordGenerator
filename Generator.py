"""
The tkinter package (“Tk interface”) is the standard Python interface to the Tk GUI toolkit.
Both Tk and tkinter are available on most Unix platforms, as well as on Windows systems.
(Tk itself is not part of Python; it is maintained at ActiveState.)
"""

from tkinter import *
from tkinter import messagebox
#This module implements pseudo-random number generators for various distributions.

import random
# initializing root
root = Tk()

# setting geometry
root.geometry("400x300")
root.title("Password Generator")
root.iconbitmap('iconfinder.ico')

# defining function to clear entry widgets using .set() method
def clear():
    Passwordlength.set("")
    Passwordtitle.set("")

# defining function to Generate a password
def Generate():

    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?><"
    passlen=Passwordlength.get()
    p =  "".join(random.sample(s,int(passlen)))
    file = open("passwd.txt", "a")
    saved=Passwordtitle.get()
    file.write(saved + ": " + str(p) + " \n")
    file.close()
    messagebox.showinfo('Passowrd', 'Password Generated sesccfully')


Passwordlength = StringVar()  # Password Length  variable
Passwordtitle = StringVar()  # Title Password variable

Label(root, text="Please enter login details").pack()
Label(root, text="").pack()
Label(root, text="how many characters").pack()
# creating an entry widget to take user length
Len_Entry = Entry(root, textvariable=Passwordlength).pack(pady=10)

Label(root, text="Tile For your Password").pack()
# creating an entry widget to take title for the password
passEntry = Entry(root, textvariable=Passwordtitle).pack(pady=10)

# creating a button to call "Generate a password" function which will print

Button(root, text='Generate', command=Generate).pack(pady=10)

# creating a button to call "clear" function which will clear the entry

Button(root, text='Clear Info', command=clear).pack(pady=10)

# .mainloop() is used when our program is ready to run

root.mainloop()

