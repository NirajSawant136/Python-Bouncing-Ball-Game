import turtle
import math
import random

gm = turtle.Screen()
gm.bgcolor('black')
gm.title('Bouncing Ball Game')
gm.tracer(0)

bd = turtle.Turtle()
bd.color('brown')
bd.width(15)
bd.penup()
bd.goto(-300,-300)
bd.left(90)
bd.pendown()
for i in range(3):
        bd.forward(600)
        bd.right(90)
bd.hideturtle()

colors = ['white' , 'skyblue' , 'orange' , 'yellow' , 'green' , 'red' , 'grey' , 'blue']

ball = turtle.Turtle()
ball.color(random.choice(colors))
ball.shape('circle')
ball.penup()
ball.speed(0)
ball.goto(random.randint(-200,200) , random.randint(0, 150))
ball.turtlesize(1.5)
ball.dx = 0.9
ball.dy = 0.7

pl = []
for i in range(3):
        pl.append(turtle.Turtle())

for i in range(3):
        pl[i].shape('square')
        pl[i].color('white')
        pl[i].penup()
        pl[i].goto(21*i,-260)

def moveLeft():
        x = pl[0].xcor()
        x -= 50
        if x < -282:
                x = -282
        for i in range(3):
                pl[i].setx(x + 21*i)

def moveRight():
        x = pl[2].xcor()
        x += 50
        if x > 282:
                x = 282
        for i in range(3):
                pl[i].setx(x - 21*(2-i))
        
score = 0
while True:
        gm.update()
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if all( (ball.xcor() <= pl[2].xcor() + 10 , ball.xcor() >= pl[0].xcor() - 10, ball.ycor()  <= -240 , ball.ycor()  >= -250) ) :
                score += 1
                ball.color(random.choice(colors))
                ball.dy *= -1
                
        if ball.xcor() < -280 or ball.xcor() > 280:
                ball.dx *= -1

        if ball.ycor() > 280:
                ball.dy *= -1
                
        if ball.ycor() < -350:
                break

        turtle.listen()
        turtle.onkey(moveLeft , 'Left')
        turtle.onkey(moveRight , 'Right')

print("YOUR  SCORE  ->   {}".format(score))

gm.mainloop()   
