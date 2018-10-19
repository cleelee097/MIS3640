import pickle

# t1=[1, 2, 3]

# f= open('save.p', 'wb')
# s= pickle.dump(t1, f)
# f.close()

# t2=pickle.load(open('save.p', 'rb'))
# print(t2)

# print(t1==t2)

def linecount(filename):
    count=0
    for line in open(filename):
        count +=1
    return count
    
if__name__=='__main'
print(linecount('wc.py'))