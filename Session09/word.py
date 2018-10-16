# fin = open("session09/words.txt")
# # line=fin.readline()
# # word=line.strip()
# # print(word)

# # counter=0
# # for line in fin:
# #     word=line.strip()
# #     counter +=1
# # print(counter)

# def avoids(word, forbidden):
#     for letter in word:
#         if letter in forbidden:
#             return False
#     return True

# def uses_all(word, required):
#     for letter in required: 
#         if letter not in word:
#             return False
#     return True

# def find_words_using_all_vowels():
#     fin=open('session09/words.txt')
#     counter=0
#     for line in fin:
#         word=line.strip()
#         if uses_all(word,'aeiou'):
#             print(word)
#             counter+=1
#     return counter
 
# print('The number of words that use all the vowels:',        find_words_using_all_vowels())
           
 
# #Return True if letter appears in alphabetical order (double letters are okay). 
# before= word[0]
# for letter in word:
#     if letter<before:
#         return False
#         before = letter
#     return True

def find_abecedarian_words():
    fin = open("session09/words.txt")
    counter=0
    current_longest = ''
    for line in fin:
        word=line.strip()
        if is_abcdedarian(word):
            print(word)
            counter+=1
            if len(word)>len(current_longest_word):
                current_longest_word=word
                print('current longest',
                current_longest_word)

    return counter, longest_word






# def read_long_words():
    
#     for line in fin:
#     word = line.strip()
#     if len(word) >20:
#         print (word)

# read_long_words()


# def has_no_e(word):
#     for letter in word:
#         if letter =='e' or letter =='E':
#             return False
#     return True


# print(has_no_e('Babson'))
# print(has_no_e('College'))



#     takes a word and a string of forbidden letters, and that returns True
#     if the word doesn’t use any of the forbidden letters.
#     """
#     pass


# print(avoids('Babson', 'ab'))
# print(avoids('College', 'ab'))


# def uses_only(word, available):
#     """
#     takes a word and a string of letters, and that returns True if the word
#     contains only letters in the list.
#     """
#     pass


# print(uses_only('Babson', 'aBbsonxyz'))
# print(uses_only('college', 'aBbsonxyz'))


# def uses_all(word, required):
#     """
#     takes a word and a string of required letters, and that returns True if
#     the word uses all the required letters at least once.
#     """
#     pass


# print(uses_all('Babson', 'abs'))
# print(uses_all('college', 'abs'))


# def is_abecedarian(word):
#     """
#     returns True if the letters in a word appear in alphabetical order
#     (double letters are ok).
#     """
#     pass


# print(is_abecedarian('abs'))
# print(is_abecedarian('college'))





