import turtle as t
import random as r
wn = t.Screen()

font_setup = ("Verdana", 30, "normal")

acorn_image = "acorn.gif" # Store the file name of your shape
basket_image = "basket.gif"

wn = t.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(acorn_image) # Make the screen aware of the new file
wn.addshape(basket_image)
wn.bgpic("forest.gif")
t.hideturtle()

score = 0

def update_score():
  counter = t.Turtle()
  counter.speed(0)
  counter.pencolor("white")
  counter.penup()
  counter.goto(-500, 250)
  counter.clear()
  counter.write(score, font=font_setup)

update_score()

wn.mainloop()
