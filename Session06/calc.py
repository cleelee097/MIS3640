# age = input('please enter your age:')
# if int(age) >= 18:
#     print('adult')
# elif int(age) >=6:
#     print('teenager')
# else:
#     print('kid')



# if x == y:
#     print('x and y are equal')
# else:
#     if x < y:
#         print('x is less than y')
#     else:
#         print('x is greater than y')
        

# import webbrowser 

# def calculate_bmi(weight, height):
#     bmi=weight/(height*hegiht)
#     if bmi<=18.5:
#         print("your bmi is {:.1f}. You are underweighted.".format (bmi))

#     elif 18.5 < bmi <= 25:
#         print('y')
#     print('Overweight')
# elif 18.5<=int(bmi)<=24.9:
#     print('Normal weight')
# else:
#     print('underweight')



# 2. Assume that two variables, varA and varB, are assigned values, either numbers or strings. 
# Write a piece of Python code that prints out one of the following messages:

# "string involved" if either varA or varB are strings
# "bigger" if varA is larger than varB
# "equal" if varA is equal to varB
# "smaller" if varA is smaller than varB

def compare(varA, varB):
    if isinstnace(varA, str) or isinstance(varB, str):
        print('string involved')
    else:
        if varA > varB:
            print('bigger')
        elif varA==varB:
            print('equal')
        else:
            print('smaller')
a='hello'
b=3
c=5

compare(a,b)
compare(b,c)




def diff21(n):
 if n<=21:
   return 21-n
  else:
    return (n-21)*2

    
#hen squirrels get together for a party, they like to have cigars. 
# A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. 
# Unless it is the weekend, in which case there is no upper bound on the number of cigars. 
# Return True if the party with the given values is successful, or False otherwise.
return is_weekend and cigars >=40 or 40 <=cigars <=60

print(cigar_party(30,False)) #False
print(cigar_party(50,False)) #True
print(cigar_party(70,False))#True




# def cigar_party(cigars, is_weekend):
#     if is_weekend and cigars
#         return True
#     else:
#         if 40<=cigars<=60:
#             return True
#         else:
#             return False
print(cigar_party(30,False)) #False
print(cigar_party(50,False)) #True
print(cigar_party(70,False))#True


def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
countdown(5)

def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)


#countdown(5)

def fabonacci(n):
    if n == 1 or n == 2:
        return 1
    return fabonacci(n-2) + fabonacci(n-1)

# print(fabonacci(6))
# print(fabonacci(2))

def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n

print(factorial(3))