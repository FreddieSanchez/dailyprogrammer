# 
#htt://www.reddit.com/r/dailyprogrammer/comments/u8jn9/5282012_challenge_58_intermediate/
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
  half_len_front = len(str_num)/2
  half_len_back = len(str_num)/2 + len(str_num)%2
  first_half = str_num[:half_len_front]
  second_half = str_num[half_len_back:][::-1]
  return first_half == second_half

def next_palindrome(num):
  # finds the next palindrome from num. 
  num+=1
  str_num = str(num)
  is_even = (len(str_num) % 2 == 0)
  half_len = len(str_num)/2
  first_half = str_num[:half_len]
  #reverse the first half
  second_half = first_half[::-1]
  middle = str_num[half_len:half_len+1]
  # concat the first half with the second, append the middle char
  # if the length of the number is odd.
  if is_even:
    new_num = first_half + second_half
  else:
    new_num = first_half + middle + second_half
  new_num = int(new_num)
  # if the new num is smaller than the old number, 
  # increment the middle digit(s)
  # example: 
  # old: 2113
  # new: 2112
  # pal: 2222
  
  # old: 132
  # new: 131
  # pal: 141
  if (new_num < num):
    new_num += 10**half_len
    if is_even:
      new_num += 10**(half_len-1)

  return new_num ; 

def main():
  if len(sys.argv) < 2:
    print "Please enter a number!\n"
    exit -1
  print next_palindrome(int(sys.argv[1]))

if __name__ == '__main__':
  main()
