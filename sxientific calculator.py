
import tkinter as tk
import math
import re

# ---------- Window ----------
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("460x640")
root.resizable(False, False)
root.configure(bg="#1e1e2e")

angle_mode = "DEG"  # DEG ya RAD

# ---------- Display ----------
display = tk.Entry(
    root,
    font=("Arial", 28, "bold"),
    bg="#e0e0e0",
    fg="#222222",
    justify="right",
    bd=0,
)
display.pack(padx=15, pady=20, fill="x", ipady=15)


# ---------- Math helpers ----------
def to_rad(x):
    return math.radians(x) if angle_mode == "DEG" else x


def sin(x): return math.sin(to_rad(x))
def cos(x): return math.cos(to_rad(x))
def tan(x): return math.tan(to_rad(x))
def fact(x): return math.factorial(int(x))


NAMESPACE = {
    "sin": sin, "cos": cos, "tan": tan,
    "log": math.log10, "ln": math.log,
    "sqrt": math.sqrt, "fact": fact,
    "pi": math.pi, "e": math.e,
}


# ---------- Functions ----------
def click(value):
    display.insert(tk.END, value)


def clear():
    display.delete(0, tk.END)


def delete():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def toggle_mode():
    global angle_mode
    angle_mode = "RAD" if angle_mode == "DEG" else "DEG"
    mode_btn.config(text=angle_mode)


def calculate():
    expr = display.get()
    try:
        expr = expr.replace("π", "pi").replace("√", "sqrt").replace("^", "**")
        # sirf allowed names aur characters chalenge (safety)
        for name in re.findall(r"[A-Za-z_]+", expr):
            if name not in NAMESPACE:
                raise ValueError
        if not re.fullmatch(r"[0-9A-Za-z_+\-*/%.() ]+", expr):
            raise ValueError
        result = eval(expr, {"__builtins__": {}}, NAMESPACE)
        if isinstance(result, float):
            result = round(result, 10)
            if result.is_integer():
                result = int(result)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Error")


# ---------- Buttons ----------
frame = tk.Frame(root, bg="#1e1e2e")
frame.pack(padx=10, pady=5, fill="both", expand=True)

NAVY = "#23284d"
ORANGE = "#e8912d"
RED = "#d9534f"
PURPLE = "#8e5bc4"
GREEN = "#2ecc71"
PINK = "#e84a8a"
GOLD = "#c9a227"
GREY = "#5d6d7e"

# (text, row, col, colspan, color, command)
buttons = [
    ("DEG", 0, 0, 1, GREY, toggle_mode),
    ("C", 0, 1, 1, RED, clear),
    ("⌫", 0, 2, 1, PURPLE, delete),
    ("(", 0, 3, 1, ORANGE, lambda: click("(")),
    (")", 0, 4, 1, ORANGE, lambda: click(")")),

    ("sin", 1, 0, 1, PINK, lambda: click("sin(")),
    ("cos", 1, 1, 1, PINK, lambda: click("cos(")),
    ("tan", 1, 2, 1, PINK, lambda: click("tan(")),
    ("π", 1, 3, 1, PINK, lambda: click("π")),
    ("e", 1, 4, 1, PINK, lambda: click("e")),

    ("log", 2, 0, 1, GOLD, lambda: click("log(")),
    ("ln", 2, 1, 1, GOLD, lambda: click("ln(")),
    ("√", 2, 2, 1, GOLD, lambda: click("√(")),
    ("x²", 2, 3, 1, GOLD, lambda: click("^2")),
    ("xʸ", 2, 4, 1, GOLD, lambda: click("^")),

    ("7", 3, 0, 1, NAVY, lambda: click("7")),
    ("8", 3, 1, 1, NAVY, lambda: click("8")),
    ("9", 3, 2, 1, NAVY, lambda: click("9")),
    ("/", 3, 3, 1, ORANGE, lambda: click("/")),
    ("n!", 3, 4, 1, GREY, lambda: click("fact(")),

    ("4", 4, 0, 1, NAVY, lambda: click("4")),
    ("5", 4, 1, 1, NAVY, lambda: click("5")),
    ("6", 4, 2, 1, NAVY, lambda: click("6")),
    ("*", 4, 3, 1, ORANGE, lambda: click("*")),
    ("%", 4, 4, 1, ORANGE, lambda: click("%")),

    ("1", 5, 0, 1, NAVY, lambda: click("1")),
    ("2", 5, 1, 1, NAVY, lambda: click("2")),
    ("3", 5, 2, 1, NAVY, lambda: click("3")),
    ("-", 5, 3, 1, ORANGE, lambda: click("-")),
    ("1/x", 5, 4, 1, GREY, lambda: click("1/(")),

    ("0", 6, 0, 1, NAVY, lambda: click("0")),
    (".", 6, 1, 1, NAVY, lambda: click(".")),
    ("=", 6, 2, 2, GREEN, calculate),
    ("+", 6, 4, 1, ORANGE, lambda: click("+")),
]

for text, r, c, span, color, cmd in buttons:
    b = tk.Button(
        frame,
        text=text,
        font=("Arial", 16, "bold"),
        bg=color,
        fg="white",
        activebackground="#ffffff",
        activeforeground="#000000",
        bd=0,
        command=cmd,
    )
    b.grid(row=r, column=c, columnspan=span, sticky="nsew", padx=3, pady=3)
    if text == "DEG":
        mode_btn = b

for i in range(5):
    frame.columnconfigure(i, weight=1)
for i in range(7):
    frame.rowconfigure(i, weight=1)

tk.Label(
    root,
    text="♥ My Scientific Calculator ♥",
    font=("Arial", 10, "bold"),
    bg="#1e1e2e",
    fg="white",
).pack(pady=8)

root.bind("<Return>", lambda e: calculate())
root.bind("<Escape>", lambda e: clear())

root.mainloop()