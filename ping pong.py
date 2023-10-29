import turtle

#Screen
screen = turtle.Screen()
screen.title("Ping Pong Game")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=8, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=8, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.4
ball.dy = -0.4

#Score
score_a = 0
score_b = 0

#Score display
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player Kanan: {}  Player Kiri: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

def update_score():
    score_display.clear()
    score_display.write("Player kanan: {}  Player Kiri: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    
#Move paddles
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 250:
        y += 100
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -240:
        y -= 100
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 250:
        y += 100
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -240:
        y -= 100
    paddle_b.sety(y)

#Keybindings
screen.listen()
screen.onkeypress(paddle_a_up, "w")
screen.onkeypress(paddle_a_down, "s")
screen.onkeypress(paddle_b_up, "Up")
screen.onkeypress(paddle_b_down, "Down")


# Main Game
while True:
    screen.update()

    # Ball moving
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collitions with walls
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Collitions with paddles
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.color("cyan")
        ball.setx(340)
        ball.dx *= -1
        update_score()

    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.color("lime")
        ball.setx(-340)
        ball.dx *= -1
        update_score()

    # Ball out of area
    if ball.xcor() > 370:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.color("white")
        score_a += 1
        score_display.clear()
        score_display.write("Player Kanan: {}  Player Kiri: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    elif ball.xcor() < -370:    
        ball.goto(0, 0)
        ball.dx *= -1
        ball.color("white")
        score_b += 1
        score_display.clear()
        score_display.write("Player Kanan: {}  Player Kiri: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
