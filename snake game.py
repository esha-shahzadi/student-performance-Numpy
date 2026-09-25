import turtle
import time
import random

# ---------------- SCREEN ----------------
screen = turtle.Screen()
screen.title("Snake Game 🐍")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# ---------------- SNAKE HEAD ----------------
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("green")
head.penup()
head.goto(0, 0)
head.direction = "right"

# ---------------- FOOD ----------------
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()

food.goto(
    random.randint(-14, 14) * 20,
    random.randint(-14, 14) * 20
)

# ---------------- SNAKE BODY ----------------
snake = []

# ---------------- SCORE ----------------
score = 0
high_score = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)

score_display.write(
    "Score: 0  High Score: 0",
    align="center",
    font=("Arial", 18, "normal")
)

# ---------------- MOVEMENT ----------------
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    elif head.direction == "down":
        head.sety(head.ycor() - 20)

    elif head.direction == "left":
        head.setx(head.xcor() - 20)

    elif head.direction == "right":
        head.setx(head.xcor() + 20)


# ---------------- KEYBOARD ----------------
screen.listen()

screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# ---------------- MAIN GAME ----------------
while True:

    screen.update()

    # Move body from back to front
    for i in range(len(snake) - 1, 0, -1):
        x = snake[i - 1].xcor()
        y = snake[i - 1].ycor()
        snake[i].goto(x, y)

    # First body part follows head
    if len(snake) > 0:
        snake[0].goto(head.xcor(), head.ycor())

    # Move snake
    move()

    # ---------------- WALL COLLISION ----------------
    if (
        head.xcor() > 280
        or head.xcor() < -280
        or head.ycor() > 280
        or head.ycor() < -280
    ):

        time.sleep(1)

        head.goto(0, 0)
        head.direction = "right"

        for segment in snake:
            segment.goto(1000, 1000)

        snake.clear()

        score = 0

        score_display.clear()
        score_display.write(
            f"Score: {score}  High Score: {high_score}",
            align="center",
            font=("Arial", 18, "normal")
        )

    # ---------------- FOOD COLLISION ----------------
    if head.distance(food) < 20:

        # Move food
        food.goto(
            random.randint(-14, 14) * 20,
            random.randint(-14, 14) * 20
        )

        # Create new body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("lightgreen")
        new_segment.penup()

        snake.append(new_segment)

        # Increase score
        score += 10

        if score > high_score:
            high_score = score

        score_display.clear()
        score_display.write(
            f"Score: {score}  High Score: {high_score}",
            align="center",
            font=("Arial", 18, "normal")
        )

    # ---------------- BODY COLLISION ----------------
    for segment in snake:

        if segment.distance(head) < 20:

            time.sleep(1)

            head.goto(0, 0)
            head.direction = "right"

            for segment in snake:
                segment.goto(1000, 1000)

            snake.clear()

            score = 0

            score_display.clear()
            score_display.write(
                f"Score: {score}  High Score: {high_score}",
                align="center",
                font=("Arial", 18, "normal")
            )

    time.sleep(0.1)

turtle.done()