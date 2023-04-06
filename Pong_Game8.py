import turtle
import time
import random

screen=turtle.Screen()
screen.title("Pong Game")
screen.setup(400,400)
turtle.bgcolor("black")
screen.tracer(0)

End=turtle.Turtle()

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

Score1=0
Score2=0
lives1=5
lives2=5
score1=turtle.Turtle()
score1.color("white")
score1.penup()
score1.setpos(-300,250)
score1.write("Player1 Score="+str(Score1),font=("Calibri",20,"bold"))
score2=turtle.Turtle()
score2.color("white")
score2.penup()
score2.setpos(100,250)
score2.write("Player2 Score="+str(Score2),font=("Calibri",20,"bold"))

Lives1=turtle.Turtle()
Lives1.color("white")
Lives1.penup()
Lives1.setpos(-300,210)
Lives1.write("Lives="+str(lives1),font=("Calibri",20,"bold"))
Lives2=turtle.Turtle()
Lives2.color("white")
Lives2.penup()
Lives2.setpos(100,210)
Lives2.write("Lives="+str(lives2),font=("Calibri",20,"bold"))
K=0
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

def Paddle2_Lives():
  Lives2.setpos(100,210)
  Lives2.clear()
  Lives2.write("Lives="+str(lives2),font=("Calibri",20,"bold"))
def Paddle1_Lives():
  Lives1.setpos(-300,210)
  Lives1.clear()
  Lives1.write("Lives="+str(lives1),font=("Calibri",20,"bold"))
  

i=0
j=0
screen.listen()
screen.onkey(Skate1_UP,"w")
screen.onkey(Skate1_DOWN,"s")
screen.onkey(Skate2_UP,"Up")
screen.onkey(Skate2_DOWN,"Down")
while(True):
  
  screen.update()
  Ball.setx(Ball.xcor()+Ball.dx)
  Ball.sety(Ball.ycor()+Ball.dy)
  if(Ball.xcor()<=-140):
    Random=random.randint(20,100)
    Paddle1.sety(Ball.ycor()+Random)
  
  
  if Ball.ycor()>220:
    Ball.sety(220)
    Ball.dy=Ball.dy*(-1)
  if Ball.ycor()<-220:
    Ball.sety(-220)
    Ball.dy=Ball.dy*(-1)
  if Ball.xcor()>400:
    Ball.goto(0,0)
    lives2=lives2-1  # one life lost
    Paddle2_Lives()
    mylist = [1,-1]
    val1= random.choice(mylist)
    Ball.dx=Ball.dx*(val1)
  if Ball.xcor()<-400:
    Ball.goto(0,0)
    lives1=lives1-1  # one life lost
    Paddle1_Lives()
    mylist = [1,-1]
    val2= random.choice(mylist)
    Ball.dx=Ball.dx*(val2)

    
    
    
  if((lives2<=0)and(Score1>Score2)):
     screen.clear()
     screen.bgcolor("black")
     End.goto(-330,0)
     End.color("white")
     End.write("Player1 Won with Score="+str(Score1),font=("Calibri",50,"bold"))
     break
  if((lives2<=0)and(Score2>Score1)):
     screen.clear()
     screen.bgcolor("black")
     End.goto(-330,0)
     End.color("white")
     End.write("Player2 Won with Score="+str(Score2),font=("Calibri",50,"bold"))
     break
  if((lives1<=0)and(Score1>Score2)):
     screen.clear()
     screen.bgcolor("black")
     End.goto(-330,0)
     End.color("white")
     End.write("Player1 Won with Score="+str(Score1),font=("Calibri",50,"bold"))
     break
  if((lives1<=0)and(Score2>Score1)):
     screen.clear()
     screen.bgcolor("black")
     End.goto(-330,0)
     End.color("white")
     End.write("Player2 Won with Score="+str(Score2),font=("Calibri",50,"bold"))
     break
  if(((lives1<=0)or(lives2<=0))and(Score1==Score2)):
     screen.clear()
     screen.bgcolor("black")
     End.goto(-330,0)
     End.color("white")
     End.write("Both Have Same Score\n    Match Tie Score="+str(Score1),font=("Calibri",50,"bold"))
     break
  
     
     
    
  if((Ball.xcor()==Paddle2.xcor()-10)and(Ball.ycor()<=Paddle2.ycor()+50)and(Ball.ycor()>=Paddle2.ycor()-50)):    
    Ball.dx=Ball.dx*(-1)
    #if(Ball.xcor()==Paddle2.xcor()-20):
    Score2=Score2+1
    score2.clear()
    score2.write("Player2 Score="+str(Score2),font=("Calibri",20,"bold"))
    

  if((Ball.xcor()==Paddle1.xcor()-10)and(Ball.ycor()<=Paddle1.ycor()+50)and(Ball.ycor()>=Paddle1.ycor()-50)): 
    Ball.dx=Ball.dx*(-1)
    score1.setpos(-300,250)
    Score1=Score1+1
    score1.clear()
    score1.write("Player2 Score="+str(Score1),font=("Calibri",20,"bold"))
    
    

screen.mainloop()



