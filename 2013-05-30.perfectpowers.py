#/usr/bin/python
import math

'''
I took into account the fact that Y is always a prime number. 
Since we are attempting to maximize 'p', we're looking for the smallest prime product Y. 
Once we have the smallest prime product, simply do a log (x) base y.
'''
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

x = int(raw_input())      
for y in list_primes():
  if x % y == 0:
    print int(math.log(x,y))
    break
    

  
