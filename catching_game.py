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
basket.goto(0,-288)
basket.speed(6)
basket.shape("basket.gif")
#bacground color
wn.bgpic("forest.gif")
#counter setting
counter = t.Turtle()
counter.hideturtle()
font_setup = ("Verdana", 50, "normal")
#list making
acorn_list = []
for i in range(100):
  acorn_list.append("acorn")


acorn_cor_list = [-740, -640, -540, -440, -340, -240, -140, -40, 60, 160, 260, 360, 460, 560, 660, 730]
acorn_speed = 2
def draw_apple(index):
  acorn_list[index].showturtle()
  random_acorn_cor = r.randint(1,15)
  acorn_list[index].penup()
  acorn_list[index].shape("acorn.gif")
  wn.tracer(False)
  acorn_list[index].speed(acorn_speed)
  acorn_list[index].setx(random_acorn_cor[random_acorn_cor])
  acorn_list[index].goto(random_acorn_cor, -500)
  wn.tracer(True)
  wn.update()



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
  x -= 40
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
