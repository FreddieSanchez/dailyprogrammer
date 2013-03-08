# 
#http://www.reddit.com/r/dailyprogrammer/comments/u8jn9/5282012_challenge_58_intermediate/
#  
#  For the easy part of today's challenge, we considered numbers that are 
#  palindromes in different bases. For this problem, lets only concern 
#  ourselves with numbers that are palindromes in base 10.
#
#  Define a function P(N) that takes as input a number N, and returns the 
#  smallest base 10 palindrome larger than N (i.e. it returns the "next" 
#  palindrome after N). So, for instance:
#
#  P(808) = 818
#  P(999) = 1001
#  P(2133) = 2222
#  What is P( 339 )?
#  BONUS: What is P( 7100 )
#  

import sys

def is_palindrome(num):
  #returns True/False if the number is palindrome.
  str_num = str(num)
  for char in range(len(str_num)/2):
    if str_num[char] != str_num[(char + 1) * -1]:
      return False
  return True

# brute force
def next_palindrome(num):
  # finds the next palindrome from num. 
  num = num + 1
  while not is_palindrome(num):
    num = num + 1

  return num; 
def main():
  if len(sys.argv) < 2:
    print "Please enter a number!\n"
    exit -1
  print next_palindrome(int(sys.argv[1]))

if __name__ == '__main__':
  main()
