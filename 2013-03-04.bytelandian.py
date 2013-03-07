#!/usr/bin/python

import sys
def bytelandian(num):
  if num == 0:
    return 1;
  return bytelandian(num/2) + bytelandian(num/3) + bytelandian(num/4)

def main():
  print bytelandian(2);
  print bytelandian(7);
  print bytelandian(1000);
  


if __name__ == '__main__':
  main()
