from tkinter import *
import datetime

def checkIt():

    file = open("usom.txt", "r")
    content = file.read()
    file.close()
    ip = entry1.get()
    now = datetime.datetime.now

    if str(ip) in content:

        file = open("log.txt", "a")
        inscription = str(ip) + " is harmful\nDate:" + str(now) + "\n"
        file.write(inscription)
        file.close()
        var.set("IP is harmful")

    else:

        file = open("log.txt", "a")
        inscription = str(ip) + " is not harmful\nDate:" + str(now) +"\n"
        file.write(inscription)
        file.close()
        var.set("IP is not harmful")

top = Tk()
top.title("USOM IP CONTROL")

B = Button(top, text="Check it", command = checkIt,)
B.place(x=40, y=40)
B.pack()

label1 = Label(top, text = "Enter the ip address to be checked:")
label1.place(x=60, y=60)
label1.pack()

entry1 = Entry(top)
entry1.place(x=80, y=90)
entry1.pack()

var = StringVar()

entry2 = Entry(top, textvariable = var)
entry2.place(x=50, y=100)
entry2.pack()

top.mainloop()
