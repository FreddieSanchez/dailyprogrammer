#!/usr/bin/python
import random

if __name__ == "__main__":
  num_dies, sides = raw_input().split('d')
  for die in range(int(num_dies)):
    print random.randrange(1,int(sides)+1),

