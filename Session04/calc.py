max (1, 2, 3, 4, 5)
round(4.5)
round(4.6)
round(4.5000000000000001)
round(4.51)
round(4.50001)

min(432, 4654, 0, 0, -123)
ord('d')
ord('c')
ord('A')
ord('.')
ord('D')
chr(46)
chr(ord('A')+3)

def print_lyrics():
    print("Hey Jude, Don't make it bad.")
    print("Take a sad song and make it better.")

# print_lyrics()

# print(type(print)lyrics))

def repeat_lyrics():
    print_lyrics()
    print('Na- na - na')
    print_lyrics()

# repeat_lyrics()

def print_twice(whatever):
    print('first time:')
    print(whatever)
    print('the second time:')
    print(whatever)

name=input('Please enter your name')
print_twice('Babson')
print(whatever)




def my_abs(n):
    if n< 0:
        print(-n)
    else:
        print(n)

my_abs(-5)
my_abs(4) 

def give_me_a_break():
    return 'break'

# print(give_a_break())
def give_me_another_break():
    strl='break'
    print('another break')
    return strl

    # print(give_me_another_break())

result= print_twice('Bing')
print(result)

    import math
def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)


import cmath

print('Solve the quadratic equation: ax**2 + bx + c = 0')
a = float(input('Enter a value : '))
b = float(input('Enter b value : '))
c = float(input('Enter c value: '))
delta = (b**2) - (4*a*c)
solution1 = (-b-cmath.sqrt(delta))/(2*a)
solution2 = (-b+cmath.sqrt(delta))/(2*a)

print('The solutions are {0} and {1}'.format(solution1,solution2))