#!/usr/bin/python

"""
http://www.reddit.com/r/dailyprogrammer/comments/1aih0v/031813_challenge_122_easy_words_with_ordered/

Find words in a word list that contain all the vowels in alphabetical order, 
non-repeated, where vowels are defined as A E I O U Y.
"""

import re, sys

def main():
  f = open(sys.argv[1],"r")
  words = f.readlines()
  f.close()

  pattern = re.compile("[aeiouy]")
  for w in words:
    word = "".join(re.findall(pattern, w))
    if word == "aeiouy":
      print w,

if __name__ == "__main__":
  main()
