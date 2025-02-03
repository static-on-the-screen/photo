from PIL import Image
from urllib.request import urlopen
import time
import turtle
def start():
    turtle.clear()
    turtle.textinput("Upload a Photo","Paste the URL of your desired photo into the box.")


s = turtle.getscreen()
turtle.hideturtle()
turtle.penup()
turtle.goto(-180, 200)
turtle.write("Photo Editing!", font=("Calibri", 45, "normal"))
turtle.penup()
turtle.goto(-130, 45)
turtle.write("Press space to start", font=("Calibri", 20, "normal"))
turtle.onkey(start,)











turtle.mainloop()