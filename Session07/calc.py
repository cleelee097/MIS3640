# result = 0

# for i in range(1, 1001):
#     print('current number to be added', i)
#     result = result + i
#     print('new result after this iteration:', result)

# print('The final result:', result)  

# break

# result = 0 
# for i in range (1,1001):
#     if i%2 ==1:
#         result = result + i
# print('the sum of odd numbers is', result)


# break

# result = 1
# for i in range (1, 11):
#     result=result*i
# print('The factorial of 10 is', result)

# break 

# import time

# def countdonw(n):
#     while n>0:
#         print(n)
#         time.sleep(1)
#         n = n-1
#     print('Blastoff!')
# countdown(5)



# iteration = 0
# count = 0
# while iteration < 5:
#     # the variable 'letter' in the loop stands for every 
#     # character, including spaces and commas!
#     for letter in "hello, world": 
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1 

# break


iteration = 0
count = 0
while iteration < 5:
    # the variable 'letter' in the loop stands for every 
    # # character, including spaces and commas!
    # for letter in "hello, world": 
    #     count += 1
    # print("Iteration " + str(iteration) + "; count is: " + str(count))
    # iteration += 1 
    

# while True:
#     line=input('>')
#     print('press "q" to quit')
#     if line=='done':
#         break
#     print(line)
#     print('Done!')



def square_root(a):
    x = a / 2.0
    while:
        y = (x + a / x) / 2

        if x == y:
            return x
        x = y
    print(square_root(1))