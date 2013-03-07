#!/usr/bin/python

import sys
def bytelandian(num):
  total = (num/2) + (num/3) + (num/4);
  if num < 12 or total <= num:
    return num 
  return bytelandian(num/2) + bytelandian(num/3) + bytelandian(num/4)

def main():
  if len(sys.argv) < 2:
    print "Please enter a number!"
  print bytelandian(int(sys.argv[1]))
  


if __name__ == '__main__':
  main()
