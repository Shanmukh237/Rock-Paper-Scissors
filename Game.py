from random import randint
from tkinter import *

from PIL import Image, ImageTk

r = Tk()
k1 = Image.open('C:\\Users\\kpran\\OneDrive\\Desktop\\djang\\images\\rock.jpg')#Change the Location Accordingly
bg1 = ImageTk.PhotoImage(k1)
k2 = Image.open('C:\\Users\\kpran\\OneDrive\\Desktop\\djang\\images\\scissors.jpg')
bg2 = ImageTk.PhotoImage(k2)
k3 = Image.open('C:\\Users\\kpran\\OneDrive\\Desktop\\djang\\images\\paper.jpg')
bg3 = ImageTk.PhotoImage(k3)
l = ['rock', 'paper', 'scissors']
u = 0#[]
c = 0#[]

la = Label(r, text = 'You Picked',font = 'noraml 20')
la.update()
la.grid(row = 1, column= 0)
lb = Label(r,text = 'Computer Picked',font = 'noraml 20')
lb.update()
lb.grid(row= 1 ,column= 2)

def score(g, f):
    ls = Label(r, text="Score:" + str(g) + "\t\tComputer Score:" + str(f), font="normal 22")
    ls.grid(row=0, column=0)
    ls.update()
    return


def rock():
    global u
    global c
    x = randint(0, 2)
    m = Label(r,image= bg1)
    m.grid(row= 2 ,column=1//2)
    if l[x] == "scissors":
        u += 1
        l1 = Label(r, text="computer picked: ", image=bg2, font="normal 10")
        l1.grid(row=2, column=2)
    elif l[x] == "rock":
        l1 = Label(r, text="computer picked: ", image=bg1, font="normal 10")
        l1.grid(row=2, column=2)
    else:
        l1 = Label(r, text="computer picked: ", image=bg3, font="normal 10")
        l1.grid(row=2, column=2)
        c += 1
    score(u, c)
    return


def paper():
    global u
    global c
    x = randint(0, 2)
    m = Label(r,image= bg3)
    m.grid(row= 2 ,column=1//2)
    if l[x] == "rock":
        l1 = Label(r, text="computer picked: ", image=bg1, font="normal 10")
        l1.grid(row=2, column=2)
        u += 1
    elif l[x] == "paper":
        l1 = Label(r, text="computer picked: ", image=bg3, font="normal 10")
        l1.grid(row=2, column=2)
    else:
        l1 = Label(r, text="computer picked: ", image=bg2, font="normal 10")
        l1.grid(row=2, column=2)
        c += 1
    score(u, c)
    return


def scissors():
    global u
    global c
    x = randint(0, 2)
    m = Label(r,image= bg2)
    m.grid(row= 2 ,column=1//2)
    if l[x] == "paper":
        l1 = Label(r, text="computer picked: ", image=bg3, font="normal 10")
        l1.grid(row=2, column=2)
        u += 1
    elif l[x] == "scissors":
        l1 = Label(r, text="computer picked: ", image=bg2, font="normal 10")
        l1.grid(row=2, column=2)
    else:
        l1 = Label(r, text="computer picked: ", image=bg1, font="normal 10")
        l1.grid(row=2, column=2)
        c += 1 
    score(u, c)
    return


def button_disable():
	b1["state"] = "disable"
	b2["state"] = "disable"
	b3["state"] = "disable"
  
  
def result():
    global u
    global c
    if c > u:
        l2 = Label(r, text="Computer won! ", font="normal 20")
    elif c == u:
        l2 = Label(r, text="Tie! ", font="normal 20")
    else:
        l2 = Label(r, text="User won! ", font="normal 20")
    l2.grid(row=5, column=2)
    button_disable()
    r.update()
 
score(u,c)
l0 = Label(r,text = 'Pick Your choice',font = 'normal 20')
l0.grid(row = 3 , column = 0)
b1 = Button(r, font="normal 20", image=bg1, compound=TOP, command=rock)
b1.grid(row=4, column=1)
b3 = Button(r, font="normal 20", image=bg3, compound=TOP, command=paper)
b3.grid(row=4, column=2)
b2 = Button(r, font="normal 20", image=bg2, compound=TOP, command=scissors)
b2.grid(row=4, column=3)
e = Button(r, text="Exit", command=result,font= 'noraml 15')
e.grid(row = 0 ,column=2)
r.mainloop()
