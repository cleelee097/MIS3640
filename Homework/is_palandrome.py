# (20 points) Write a recursive function isPalindrome(string) that returns True if string is a palindrome, 
# that is, a word that is the same when reversed. Examples of palindromes are “deed”, “rotor”, or “aibohphobia”. 
# Hint: A word is a palindrome if the frst and last letters match and the remainder is also a palindrome.
def isPalindrome(string):
  return string==string[::-1]
print(isPalindrome('rotor'))