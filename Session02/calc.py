# The volume of a sphere with radius r is
# (4/3)πr3. What is the volume of a sphere with radius 5?
print((4/3)*3.14*5*3) #volume of a sphere

# Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. 
# Shipping costs $3 for the first copy and 75 cents for each additional copy. 
# What is the total wholesale cost for 60 copies?
cover_price = 24.95
num_books = 60.0
bulk_book_cost = ((cover_price * 0.60) * num_books)
shipping_cost = (3.0 + (0.75 * (num_books - 1)))
print(bulk_book_cost+shipping_cost) #total wholesale cost

# If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), 
# then 3 miles at tempo (7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?
start_time_hr = 6 + 52 / 60.0
easy_pace_hr = (8 + 15 / 60.0 ) / 60.0
tempo_pace_hr = (7 + 12 / 60.0) / 60.0
running_time_hr = 2 * easy_pace_hr + 3 * tempo_pace_hr
breakfast_hr = start_time_hr + running_time_hr
breakfast_min = (breakfast_hr-int(breakfast_hr))*60
breakfast_sec= (breakfast_min-int(breakfast_min))*60

print ('breakfast_hr', int(breakfast_hr) )
print ('breakfast_min', int (breakfast_min) )
print ('breakfast_sec', int (breakfast_sec) )



# If my average grade rises from 82 to 89. 
# What is the percentage of the increase? Format the result as 'xx.x%'. Keep one figure after decimal point.
old_grade = 82
new_grade = 89
(89/82)     
print ('the increase is {:.1f}%'.format(108.53658536585367))

