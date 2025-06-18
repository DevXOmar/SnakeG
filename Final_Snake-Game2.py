from turtle import Turtle, Screen
import random
import time

head = Turtle()
head.shape("square")
head.color("red")
head.direction = "stop"  # Initialize direction attribute; A new attribute that needs to be initialized
head.penup()
head.speed(20)

screen = Screen()
screen.screensize(600, 600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)  ## Solved a Major issue.

food = Turtle()
food.shape("circle")
food.color("green")
food.penup()

High_score = 0
score_board1 = Turtle()
score_board1.goto(200, 290)
score_board1.hideturtle()
score_board1.penup()
score_board1.color("white")
score_board1.write(f"HIGH SCORE : {High_score}", align="center", font=("Ariel", 20, "normal"))

score = 0
score_board = Turtle()
score_board.goto(0, 290)
score_board.hideturtle()
score_board.penup()
score_board.color("white")


def up():
    if head.direction != "down":
        head.direction = "up"


def down():
    if head.direction != "up":
        head.direction = "down"


def left():
    if head.direction != "right":
        head.direction = "left"


def right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
    # time.sleep(0.01)

segments = []
game_running = True

counter = "Y"

def reset():
    head.goto(0,0)
    for item in segments:
        item.goto(900,900)
    segments.clear()

def consent():
    counter = screen.textinput("Alert! ","Do you wish to continue? (Y/N): ")
    return counter

while game_running:
    screen.update()

    screen.listen()
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")

    # Food Collision
    if head.distance(food) < 16:
        xcoor = random.randint(-200, 200)
        ycoor = random.randint(-200, 200)
        food.goto(xcoor, ycoor)
        score += 1
        score_board.clear()

        new_segment = Turtle("square")
        new_segment.color("red")
        new_segment.penup()
        new_segment.speed(0)  # Almost solved the animation issue of new segment joining body.
        segments.append(new_segment)

    # Wall Collision
    if head.xcor() > 320 or head.xcor() < -320 or head.ycor() > 320 or head.ycor() < -320:
        # game_running = False
        # head.direction = "stop"
        if consent() == "Y":
            reset()
        else:
            game_running = False

        if score > High_score :
            High_score = score
            score_board1.clear()
            score_board1.write(f"HIGH SCORE : {High_score - 1}", align="center", font=("Ariel", 20, "normal"))
            score = 1

    # main Snake like movement of the snake.
    for i in range(len(segments) - 1, 0, -1):
        xcur = segments[i - 1].xcor()
        ycur = segments[i - 1].ycor()
        segments[i].goto(xcur, ycur) ##

        # Self-Collision
        if head.distance(segments[i]) == 0:
            # head.direction = "stop"

            if score > High_score:
                High_score = score
                score_board1.clear()
                score_board1.write(f"HIGH SCORE : {High_score - 1}", align="center", font=("Ariel", 20, "normal"))
                score = 1
            if consent() == "Y":
                reset()
                break
            else:
                game_running = False


    if game_running == False:
        screen1 = Turtle()
        screen1.color("white")
        screen1.write("Game Over!", align="center", font=("Ariel", 32, "normal"))
    if len(segments) > 0:
        xcur = head.xcor()
        ycur = head.ycor()
        segments[0].goto(xcur, ycur)
    move()
    score_board.clear()
    score_board.write(f"SCORE : {score - 1}", align="center", font=("Ariel", 20, "normal"))

    # score_board1.write(f"HIGH SCORE : {High_score-1}", align="center", font=("Ariel", 20, "normal"))
    time.sleep(0.1)

screen.mainloop()  # Keeps the window open and handles events like key presses.