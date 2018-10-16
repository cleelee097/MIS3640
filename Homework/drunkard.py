import turtle
import random

drunkard=turtle.Turtle()
def go_right(step):
     drunkard.setheading(0)
     drunkard.forward(step)

def go_up(step):
     drunkard.setheading(90)
     drunkard.forward(step)


def go_left(step):
     drunkard.setheading(180)
     drunkard.forward(step)

def go_down(step):
     drunkard.setheading(270)
     drunkard.forward(step)

def drunkard_walk(step_size, step_number):
    move_dict = {1: go_up,
                 2: go_right,
                 3: go_left,
                 4: go_down
                 }
    for _ in range(step_number):
        move_in_a_direction = move_dict[random.randint(1, 4)]
        move_in_a_direction(step_size)

if __name__ == "__main__":
    drunkard_walk(15, 100)