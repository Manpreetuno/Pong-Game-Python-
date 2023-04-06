import turtle

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

while(True):
  
  screen.update()

screen.mainloop()



