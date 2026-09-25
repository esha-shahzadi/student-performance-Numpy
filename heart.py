import turtle
import math
import random

# Screen setup
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Colorful Heart")

# Turtle setup
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.pensize(2)

colors = ["red", "blue", "lime", "yellow", "magenta", "pink", "cyan", "orange"]

# Draw the heart
for i in range(180):
    t.penup()
    
    # Parametric heart equation
    angle = math.pi * 2 * i / 180

    x = 16 * math.sin(angle) ** 3
    y = (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    )

    # Make it bigger
    x *= 15
    y *= 15

    # Random color
    t.color(random.choice(colors))

    # Draw a line from the center to the heart
    t.goto(0, 0)
    t.pendown()
    t.goto(x, y)

    # Small star-like effect
    t.penup()
    t.goto(x, y)
    t.dot(6, random.choice(colors))

turtle.done()


# import time
# import sys
# import os

# # Colors
# GREEN = "\033[92m"
# CYAN = "\033[96m"
# YELLOW = "\033[93m"
# MAGENTA = "\033[95m"
# BLUE = "\033[94m"
# RESET = "\033[0m"
# BOLD = "\033[1m"


# def typing(text, color):
#     for ch in text:
#         sys.stdout.write(f"{BOLD}{color}{ch}{RESET}")
#         sys.stdout.flush()
#         time.sleep(0.05)
#     print()


# def run_song():
#     os.system("cls" if os.name == "nt" else "clear")

#     typing("♪ Suhani Nagar Mein ♪", GREEN)
#     time.sleep(0.8)

#     typing("Tumhari Nazar Mein 💕", CYAN)
#     time.sleep(0.8)

#     typing("Khayalon Ki Duniya...", MAGENTA)
#     time.sleep(0.8)

#     typing("♪ ❤️ ♪", YELLOW)


# # run_song()

# import time
# import sys
# import pyttsx3

# # Text-to-Speech setup
# engine = pyttsx3.init()
# engine.setProperty("rate", 140)
# engine.setProperty("volume", 1.0)

# # Colors
# GREEN = "\033[92m"
# CYAN = "\033[96m"
# YELLOW = "\033[93m"
# MAGENTA = "\033[95m"
# RESET = "\033[0m"
# BOLD = "\033[1m"


# def sing_line(text, color):
#     # Print the line character by character
#     for ch in text:
#         sys.stdout.write(f"{BOLD}{color}{ch}{RESET}")
#         sys.stdout.flush()
#         time.sleep(0.04)

#     print()

#     # Speak the same line
#     engine.say(text)
#     engine.runAndWait()


# def run_song():
#     print()

#     sing_line("♪ Suhani Nagar Mein ♪", GREEN)
#     time.sleep(0.5)

#     sing_line("Tumhari Nazar Mein", CYAN)
#     time.sleep(0.5)

#     sing_line("Khayalon Ki Duniya Basayenge Hum", MAGENTA)
#     time.sleep(0.5)

#     sing_line("♪ ❤️ ♪", YELLOW)


# run_song()