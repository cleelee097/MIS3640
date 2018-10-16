team = 'New England Patriots'
len(team)
print(team[1,5])
print(team[0])
team[1,0]
team[20-1]
team[len(team)-1]
team[-1]
team[-2]
team[-20]
team[0:3]
team[:11]
team[11:4]
team[::2]
team[::-2]  

print(find(team, 'a'))




# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter=='O' or letter =='Q':
#     print(letter + 'u' +suffix)
#     else:
#         print(letter+suffix)


# for i, letter in enumerate(team):
    # print(i,letter)


# word = 'New England Patriots'
# count = 0
# for letter in word:
#     if letter == 'a':
#         count = count + 1
# print(count)

def count(s, letter):
    c = 0
    for each in s:
        if each ==letter:
            c+=1
    return c

print(count(team,'a')) #should be 2
print(count(team, ' '))



