#!/usr/bin/python

import sys
c = {}
def bytelandian(num):
  total = (num/2) + (num/3) + (num/4);
  if total <= num:
    return num
  if num not in c:
    c[num] = bytelandian(num/2) + bytelandian(num/3) + bytelandian(num/4)
  return c[num];

def main():
  if len(sys.argv) < 2:
    print "Please enter a number!"
    return -1;
  print bytelandian(int(sys.argv[1]))
  return 0

if __name__ == '__main__':
  main()
