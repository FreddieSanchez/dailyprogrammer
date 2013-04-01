#!/usr/bin/python

def digital_root(number):
  if number < 10:
    return number
  sum = 0
  for x in range(len(str(number)))[::-1]:
    q,r = divmod (number,10**x)
    number = r
    sum += q 
  return digital_root(sum)

if __name__ == "__main__":
  number = int(raw_input())
  print digital_root(number)
