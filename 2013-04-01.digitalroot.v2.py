#!/usr/bin/python

# congruence formula
def digital_root(number):
  return 1 + (number-1)%9

if __name__ == "__main__":
  number = int(raw_input())
  print digital_root(number)
