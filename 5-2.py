import math

def my_abs(x):
    if not isinstance(x,(int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(55))

def move(x, y, step, angle = 0):
    nx = x +step*math.cos(angle)
    ny = y +step*math.sin(angle)
    return nx,ny

print(move(100, 100, 60, math.pi / 6))

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(b*b - 4*a*c)) / (2 * a)
    x2 = (-b - math.sqrt(b*b - 4*a*c)) / (2 * a)
    return x1, x2

print(quadratic(1, 3, -4))