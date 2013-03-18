#!/usr/bin/python
import re, sys

def main():
  f = open(sys.argv[1],"r")
  words = f.readlines()
  f.close()

  pattern = re.compile(".*a.*e.*i.*o.*u.*y.*")
  for w in words:
    m = re.search(pattern, w)
    if m:
      print m.group()

if __name__ == "__main__":
  main()
