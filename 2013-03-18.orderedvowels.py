#!/usr/bin/python
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
