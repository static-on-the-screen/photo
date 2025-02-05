from PIL import Image
from urllib.request import urlopen
import time
import turtle


def choosephoto():
    x = turtle.textinput("Upload a Photo", "Paste the URL of your desired photo into the box.")
    global img
    img = Image.open(urlopen(x))
    img.show()
    y = turtle.textinput("Confirm", "Is this the photo you want? (Type yes or no)")
    if y == "yes" or "Yes":
        return img
    elif y == "no" or "No":
        return -1
    elif y == "maybe" or "Maybe" or "idk" or "Idk" or "i don't know" or "I don't know":
        turtle.textinput("What", "What do you mean you DON'T KNOW? This is YOUR photo!")
        z = turtle.textinput("Make up your mind", "So, is this the right image or not? Yes OR no?")
        if z == "yes" or "Yes":
            return img
        elif z == "no" or "No":
            return -1
        elif z == "maybe" or "Maybe" or "idk" or "Idk" or "i don't know" or "I don't know":
            turtle.textinput("", "...")
            turtle.textinput("", "Look man, I'm just trying to do my job.")
            turtle.textinput("I hate minimum wage", "I work 24 hours a day!!! 24!!")
            turtle.textinput(":/", "If you won't take this seriously, I won't waste my time.")
            turtle.textinput("Good riddance", "So long, sucker! Go download GIMP or something, because I'm not helping you!")
            exit()


turtle.hideturtle()
turtle.penup()
turtle.goto(-180, 200)
turtle.write("Photo Editing!", font=("Calibri", 45, "normal"))
turtle.penup()
turtle.goto(-130, 45)
turtle.write("Press space to start", font=("Calibri", 20, "normal"))
time.sleep(3)
turtle.clear()
x = turtle.textinput("Upload a Photo", "Paste the URL of your desired photo into the box.")
img = Image.open(urlopen(x))
img.show()


turtle.mainloop()
while True:
    img = choosephoto()
    if img == -1:
        continue
    else:
        break