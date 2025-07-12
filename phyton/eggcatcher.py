from tkinter import Canvas, Tk, messagebox, font
from random import randrange
from itertools import cycle

canwd = 400
canhg = 400

root = Tk()
root.title("egg hunt")
c = Canvas(root,width= canwd,height= canhg,background= "blue")
c.create_rectangle(-5,canwd+5,canhg-100,fill= "green",width= 0)
c.create_oval(-80,-80,120,120,fill= "yellow",width= 10)
c.pack()

eggscolor = cycle(["lightblue", "lightgray", "lightgreen","lightyellow"])
eggwd = 45
egghg = 55
eggscore = 10

speed = 500
egginterval = 4000
difficulty = 0.95

bowlcolor = "red"
bowlwd = 100
bowlhg = 100

bowlstartx = canwd/2 - canwd/2
bowlstartx2 = bowlstartx + canwd
bowlstarty = canhg - canhg-20
bowlstarty2 = bowlstarty + bowlhg

bowl = c.create_arc(bowlstartx, bowlstarty, bowlstartx2, bowlstarty2, start = 200, extend = 140, style = "arc", outline = bowlcolor, width= 3 )

gamefont = font.nametofont("Arial")
gamefont.config(size= 18)






























root.mainloop()