import turtle as t
import random as r
wn = t.Screen()
#shapes
wn.addshape("acorn.gif")
wn.addshape("basket.gif")
#basket setup
basket = t.Turtle()
basket.penup()
basket.speed(0)
basket.goto(0,-305)
basket.speed(6)
basket.shape("basket.gif")
#bacground color
wn.bgpic("forest.gif")
#counter setting
counter = t.Turtle()
counter.hideturtle()
font_setup = ("Verdana", 50, "normal")




wn = t.Screen()
wn.setup(width=1.0, height=1.0)

score = 0

def update_score():
  counter.speed(0)
  counter.pencolor("white")
  counter.penup()
  counter.goto(-500, 200)
  counter.clear()
  counter.write(score, font=font_setup)

# Basket Movement
def basket_control():
  wn.onkey()

update_score()

#each movements
def move_left():
  x = basket.xcor()
  x -= 20
  basket.setx(x)
  
def move_right():
  x = basket.xcor()
  x += 40
  basket.setx(x)

#keypress

wn.onkeypress(move_left,"a")
wn.onkeypress(move_right, "d")



wn.listen()
wn.mainloop()
