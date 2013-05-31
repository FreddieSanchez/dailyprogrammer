#/usr/bin/python
import math

def is_prime(n):
  for x in range(2,int(n**.5) + 1):
    if n % x == 0:
      return False
  return True

def list_primes():
  n = 2
  while True:
    if is_prime(n):
      yield n
    n+=1

def infinity():
  i = 1
  while True:
    yield i
    i += 1

x = int(raw_input())      
for y in list_primes():
  if x % y == 0:
    print int(math.log(x,y))
    break
    

  
