# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter=='O' or letter =='Q':
#     print(letter + 'u' +suffix)
#     else:
#         print(letter+suffix)

price = input("Enter Price ")
cash = input("Enter Cash ")
coins = [100, 50, 20, 10, 5, 1, 0.5]
change = cash-price
i = 0
while i<len(coins):
    print int(change/coins[i]),str(" X "),coins[0+i]
    if change>0:
        change = change-(int(change/coins[i])*coins[i])
    else:
        change = max(change,0)
    i=i+1