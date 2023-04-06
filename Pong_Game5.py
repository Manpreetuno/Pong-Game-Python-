import turtle
import time
import random

screen=turtle.Screen()
screen.title("Pong Game")
screen.setup(400,400)
turtle.bgcolor("black")
screen.tracer(0)

Paddle1=turtle.Turtle()
Paddle1.speed(0)
Paddle1.penup()
Paddle1.color("white")
Paddle1.goto(-210,0)
Paddle1.shape("square")
Paddle1.shapesize(5,1)


Paddle2=turtle.Turtle()
Paddle2.speed(0)
Paddle2.penup()
Paddle2.color("white")
Paddle2.goto(200,0)
Paddle2.shape("square")
Paddle2.shapesize(5,1)

Ball=turtle.Turtle()
Ball.color("gold")
Ball.speed(0)
Ball.penup()
Ball.goto(0,0)
Ball.shape("circle")
Ball.dx=0.5
Ball.dy=0.5
val1=0
val2=0
def Skate1_UP():
  y=Paddle1.ycor()
  Paddle1.sety(y+10)
  print(Paddle1.xcor())


def Skate1_DOWN():
  y=Paddle1.ycor()
  Paddle1.sety(y-10)
  print(Paddle1.xcor())

def Skate2_UP():
  y=Paddle2.ycor()
  Paddle2.sety(y+10)


def Skate2_DOWN():
  y=Paddle2.ycor()
  Paddle2.sety(y-10)


  
screen.listen()
screen.onkey(Skate1_UP,"w")
screen.onkey(Skate1_DOWN,"s")
screen.onkey(Skate2_UP,"Up")
screen.onkey(Skate2_DOWN,"Down")
while(True):
  
  screen.update()
  Ball.setx(Ball.xcor()+Ball.dx)
  Ball.sety(Ball.ycor()+Ball.dy)
  Paddle1.sety(Ball.ycor())
  if Ball.ycor()>220:
    Ball.sety(220)
    Ball.dy=Ball.dy*(-1)
  if Ball.ycor()<-220:
    Ball.sety(-220)
    Ball.dy=Ball.dy*(-1)
  if Ball.xcor()>400:
    Ball.goto(0,0)
    mylist = [1,-1]
    val1= random.choice(mylist)
    Ball.dx=Ball.dx*(val1)
  if Ball.xcor()<-400:
    Ball.goto(0,0)
    mylist = [1,-1]
    val2= random.choice(mylist)
    Ball.dx=Ball.dx*(val2)
  
  if(((Ball.pos()[0]>=Paddle2.pos()[0]-10)and(Ball.pos()[0]<=Paddle2.pos()[0]+10))and((Ball.pos()[1]>=Paddle2.pos()[1]-50)and(Ball.pos()[1]<=Paddle2.pos()[1]+50))):
    Ball.dx=Ball.dx*(-1)
  if(((Ball.pos()[0]>=Paddle1.pos()[0]-10)and(Ball.pos()[0]<=Paddle1.pos()[0]+10))and((Ball.pos()[1]>=Paddle1.pos()[1]-50)and(Ball.pos()[1]<=Paddle1.pos()[1]+50))):
    Ball.dx=Ball.dx*(-1)
    

screen.mainloop()



