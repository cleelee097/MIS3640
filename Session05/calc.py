import turtle
import math

def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)

jack=turtle.Turtle()

square(jack)

turtle.mainloop()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

jack=turtle.Turtle()

square(jack,200)
turtle.mainloop()


def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t,r):
    circumference=2*math.pi*r
    n= 50
    length=circumference/n
    polygon(t, length, n)

jack=turtle.turtle()

polygon(jack,7,70)
turtle.mainloop()


polygon(jack, n=7, length=70)
tutle.mainloop()


def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


def arc(t, r, angle):
    arc_length= 2*math.pi*r*angle/360
    n=int(arc_length/3)+1
    step_length=arc_length/n
    step_angle=angle/n

    for i in range(n):
        t.fd(step.length)
        t.let(step_angle)




