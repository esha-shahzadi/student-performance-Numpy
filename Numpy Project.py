import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 3*x + 2

def forward_diff(f,x,h):
    return (f(x+h) - f(x))/h

def backward_diff(f,x,h):
    return (f(x) - f(x-h))/h

def central_diff(f,x,h):
    return (f(x+h) - f(x-h))/(2*h)

def second_diff(f,x,h):
    return (f(x+h) - 2*f(x) + f(x-h))/(h**2)

x0 = 2
h = 0.1

true_derivative = 2*x0 + 3

fwd = forward_diff(f,x0,h)
bwd = backward_diff(f,x0,h)
cen = central_diff(f,x0,h)
sec = second_diff(f,x0,h)

print("At x =" , x0)
print("True derivative",true_derivative)
print("forward derivative",forward_diff)
print("backward derivative",backward_diff)
print("central derivative",central_diff)
print("second derivative",second_diff)
  
# task  2

import numpy as np

h_values = [0.5, 0.1, 0.01]

for h in h_values:

    forward = forward_diff(f, x0, h)
    backward = backward_diff(f, x0, h)
    central = central_diff(f, x0, h)

    forward_error = abs(forward - true_derivative)
    backward_error = abs(backward - true_derivative)
    central_error = abs(central - true_derivative)

    print("\nh =", h)

    print("Forward Error:", forward_error)
    print("Backward Error:", backward_error)
    print("Central Error:", central_error)

# task 3

import numpy as np

def f(x):
    return np.sin(x)

def second_diff(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h)) / h**2

x = np.pi / 3
h = 0.1

numerical = second_diff(f, x, h)

analytical = -np.sin(x)

print("Numerical Second Derivative:", numerical)
print("Analytical Second Derivative:", analytical)

print("Error:", abs(numerical - analytical))

#  task 4

import numpy as np

def f(x):
    return np.sin(x)


# Midpoint Rule
def midpoint_rule(f, a, b, n):

    h = (b - a) / n
    total = 0

    for i in range(n):
        x_mid = a + h * (i + 0.5)
        total += f(x_mid)

    return h * total


# Left Rectangle Rule
def left_rectangle(f, a, b, n):

    h = (b - a) / n
    total = 0

    for i in range(n):
        x = a + i * h
        total += f(x)

    return h * total


# Right Rectangle Rule
def right_rectangle(f, a, b, n):

    h = (b - a) / n
    total = 0

    for i in range(n):
        x = a + (i + 1) * h
        total += f(x)

    return h * total


# Trapezoidal Rule
def trapezoidal_rule(f, a, b, n):

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)

    y = f(x)

    I = (h / 2) * (
        y[0] +
        2 * np.sum(y[1:-1]) +
        y[-1]
    )

    return I


# Simpson 1/3 Rule
def simpsons_one_third(f, a, b, n):

    if n % 2 != 0:
        raise ValueError("n must be even")

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)

    y = f(x)

    I = (h / 3) * (
        y[0]
        + 4 * np.sum(y[1:n:2])
        + 2 * np.sum(y[2:n-1:2])
        + y[n]
    )

    return I


# Simpson 3/8 Rule
def simpsons_three_eighth(f, a, b, n):

    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3")

    h = (b - a) / n

    x = np.linspace(a, b, n + 1)

    y = f(x)

    I = (3 * h / 8) * (
        y[0]
        + 3 * np.sum(y[1:n][np.arange(1, n) % 3 != 0])
        + 2 * np.sum(y[3:n:3])
        + y[n]
    )

    return I


# Values
a = 0
b = np.pi
n = 12

exact = 2

mid = midpoint_rule(f, a, b, n)
left = left_rectangle(f, a, b, n)
right = right_rectangle(f, a, b, n)
trap = trapezoidal_rule(f, a, b, n)
simp13 = simpsons_one_third(f, a, b, n)
simp38 = simpsons_three_eighth(f, a, b, n)

print("Exact Value:", exact)
print("Midpoint:", mid)
print("Left Rectangle:", left)
print("Right Rectangle:", right)
print("Trapezoidal:", trap)
print("Simpson 1/3:", simp13)
print("Simpson 3/8:", simp38)