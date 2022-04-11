# Pong in Python 3 
# By @ManikLakherwal
# On 26-03-2022 


import turtle
import winsound

wn=turtle.Screen()
wn.title("The classic pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a=0
score_b=0


# Paddle for player A
paddle_a=turtle.Turtle()
paddle_a.speed(0)     # set the speed of animation not the paddle speed to maximum possible 
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("white")
paddle_a.penup()      # turtle draws line as it moves so this command prevent it from doing so
paddle_a.goto(-350,0)

# Paddle for player b
paddle_b=turtle.Turtle()
paddle_b.speed(0)     # set the speed of animation not the paddle speed to maximum possible 
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()      # turtle draws line as it moves so this command prevent it from doing so
paddle_b.goto(+350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)     # set the speed of animation not the paddle speed to maximum possible 
ball.shape("square")
ball.color("white")
ball.penup()      # turtle draws line as it moves so this command prevent it from doing so
ball.goto(0,0)
ball.dx=0.2
ball.dy=0.2

# Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0",align='center', font=("courier",24,"normal"))

#Function to move the paddle up
def paddle_a_up():
    y=paddle_a.ycor()    # this command pass the current position of the paddle a 
    y +=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()    # this command pass the current position of the paddle a 
    y +=20
    paddle_b.sety(y)


#Function to move the paddle down
def paddle_a_down():
    y=paddle_a.ycor()    # this command pass the current position of the paddle a 
    y -=20
    paddle_a.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()    # this command pass the current position of the paddle a 
    y -=20
    paddle_b.sety(y)



# Keyboard binding
wn.listen()         # this line says listen to the keyboard
wn.onkeypress(paddle_a_up,"w")     # when w is pressed paddle_a_up function is called an paddle moves up
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up,"Up")     
wn.onkeypress(paddle_b_down,"Down") 


# Main game loop
while True:
    wn.update()    #every time the loop run it updates the screen

    # move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # boarder checking
    if ball.ycor()>290:    # when ball touch upper boundary it bounce 
        ball.sety(290)
        ball.dy *=-1       # reverse the ball direction
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    
    if ball.ycor()< -290:  # when ball touch lower boundary it bounce 
        ball.sety(-290)
        ball.dy *=-1  
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
    if ball.xcor()> 390:   #when the ball hit hit the right side missing the paddle it returns to the center
        ball.goto(0,0)
        score_a +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align='center', font=("courier",24,"normal"))
                
    if ball.xcor()< -390:
        ball.goto(0,0)
        score_b +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a,score_b),align='center', font=("courier",24,"normal"))

    # Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor()< paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() >-350) and (ball.ycor()< paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav",winsound.SND_ASYNC)
        