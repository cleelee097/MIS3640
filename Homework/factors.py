
# Please read Code Grading Rubric (in Blackboard - Assignment) carefully before you start this assignment.

# (20 points) Factoring of integers. Write a program that asks the user for an integer and then prints 
# out all its factors.
# For example, when the user enters 150, the program should print 2 3 5 5

def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
        print(i)
print(print_factors(150))

