# def print_twice(whatever_name):
#     print(whatever_name)
#     print(whatever_name)
# print_twice('Babson')
# my_name = 'Jack'
# print_twice(my_name)

# def cat_twice(part1, part2):
#     cat = part1 + part2
#     print_twice(cat)

# line1 = 'Bing tiddle '
# line2 = 'tiddle bang.'
# cat_twice(line1, line2)

# print(cat)


# import turtle
# jack = turtle.Turtle()
# def square (t, length):
#     t.fd(100)
#     t.lt(90)
#     t.fd(100)
#     t.lt(90)
#     t.fd(100)
#     t.lt(90)
#     t.fd(100)
# square(jack, 100)

# import turtle
# jack=turtle.Turtle()
# def polygon(t, n, length):
#     angle = 360 / n
#     for i in range(n):
#         t.fd(length)
#         t.lt(angle)
# polygon(jack, 7, 70)

import turtle
import math
jack= turtle.Turtle()


def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

circle(jack,100)
turtle.mainloop()


def arc(t, r, angle):
    arc_length = 2 * math.pi * r  * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)


