# def nested_sum(t):
#     """Computes the total of all numbers in a list of lists.
#     t: list of list of numbers
#     returns: number
#     Expected output:
#      t = [[1, 2], [3], [4, 5, 6]]
#      nested_sum(t)
#      21
#      """
#     return


# def cumsum(t):
#     """Computes the cumulative sum of the numbers in t.
#     t: list of numbers
#     returns: list of numbers
#     Expected output:
#     >>> t = [1, 2, 3]
#     >>> cumsum(t)
#     [1, 3, 6]
#     """
#     return



# def middle(t):
    
    
#     """Returns all but the first and last elements of t.
#     t: list
#     returns: new list
#     Expected output:
#     >>> t = [1, 2, 3, 4]
#     >>> middle(t)
#     [2, 3]
#     """
#     return t[1:-1]


# t = [1, 2, 3, 4, 5, 7]
# print(middle(t), "the memory address of middle(t) is", id(middle(t)))

# print(t, "the memory address of  is t", id(t))


# def chop(t):
#     """Removes the first and last elements of t.
#     t: list
#     returns: None
#     Expected output:
#     >>> t = [1, 2, 3, 4]
#     >>> chop(t)
#     >>> t
#     [2, 3]
#     """
#     t.remove()

# t = [1, 2, 3, 4]
# chop(t)
# print(t)


# def is_sorted(t):
#     previous=t[0]
#     for c in t:
#         if c<previous:
#             return False
#         previous = c
#         return True
# print(is_sorted(['a']))

#     """Checks whether a list is sorted.
#     t: list
#     returns: boolean
#     Expected output:
#     >>> is_sorted([1, 2, 2])
#     True
#     >>> is_sorted(['b', 'a'])
#     False
#     """
#     return


# def is_anagram(word1, word2):
#     """Checks whether two words are anagrams
#     Two words are anagrams if you can rearrange the letters from one to 
#     spell the other.
#     word1: string or list
#     word2: string or list
#     returns: boolean
#     Expected output:
#     >>> is_anagram('stop', 'pots')
#     True
#     >>> is_anagram('different', 'letters')
#     False
#     >>> is_anagram([1, 2, 2], [2, 1, 2])
#     Ture"""
    
#     return sorted(word1)==sorted(word2)
#     print(is_anagram('stop','pots'))


# def has_duplicates(s):
#     """Returns True if any element appears more than once in a sequence.
#     s: string or list
#     returns: bool
#     output:
#     >>> print(has_duplicates('cba'))
#     False
#     >>> print(has_duplicates('abba'))
#     True
#     """
#     for x in s:
#         if s.count(x)>1:
#             return True
#         return False
   


# def has_adjacent_duplicates(s):
#     """Returns True if there are two same adjacent elements.
#     s: string or list
#     returns: bool
#     output:


#     >>> print(has_adjacent_duplicates('cba'))
#     False
#     >>> print(has_adjacent_duplicates('abca'))
#     Flase
#     >>> print(has_adjacent_duplicates('abbc'))
#     True
#     """
#     for i in range(len(s)-1):
#         if s[i]==s[i+1]
#         return True
#     return False
    


# def main():
#     t = [[1, 2], [3], [4, 5, 6]]
#     # print(nested_sum(t))

#     # t = [1, 2, 3]
#     # print(cumsum(t))

#     # t = [1, 2, 3, 4]
#     # print(middle(t))
#     # chop(t)
#     # print(t)

#     # print(is_sorted([1, 2, 2]))
#     # print(is_sorted(['b', 'a']))

#     # print(is_anagram('stop', 'pots'))
#     # print(is_anagram('different', 'letters'))
#     # print(is_anagram([1, 2, 2], [2, 1, 2]))

#     # print(has_duplicates('cba'))
#     # print(has_duplicates('abba'))


# if __name__ == '__main__':
#     main()


# def is sorted(t):
#     t.sort()
#     return t==t.sort()
# print(is_sorted)(['a','b','b','d'])
# print(is_sorted)(['a','b','c','d'])



# def histogram(s):
#     d = dict()
#     for c in s:
#         if c not in d:
#             d[c] = 1
#         else:
#             d[c] += 1
#     return d
# h = histogram('Bookkeeper')
# print(h)



# def fib(n):
#     global numFibCalls
#     numFibCalls += 1
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return fib(n - 1) + fib(n - 2)


# known = {1: 1, 2: 2}


# def fib_efficient(n):
#     global numFibCalls
#     numFibCalls += 1
#     if n in known:
#         return known[n]
#     else:
#         ans = fib_efficient(n - 1) + fib_efficient(n - 2)
#         known[n] = ans
#         return ans


# numFibCalls = 0
# fibArg = 10

# print(fib(fibArg))
# print('function calls', numFibCalls)

# numFibCalls = 0


# print(fib_efficient(fibArg))
# print('function calls', numFibCalls)



a=[1,2,3,4,5,6]
a[0]
a[:3]
a[-4]
a[:]
a[::2]
a[::-2]
a=list('Defne')
a
a[1:3]
a[:-1]

#dictionary
d={'a': 2, 'b': 3}
d['a']
d
d['d']=5
d
5 in d
'a' in d
'd' in d
5 in d.values()
d.values()

d.get('c',0)

for k in d:
    print(d, d[k])

for v in d.values():
    print(v)

