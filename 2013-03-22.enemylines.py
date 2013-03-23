#!/usr/bin/python
import sys

def depth_first(guests,table):
  table[1] = True
  for v in range(1,len(guests)):
    if table[v] != None:
      next
    stack = [v]
    while len(stack):
      guest = stack.pop()
      for enemy in guests[guest]:
        if table[enemy] == None:
          # put the enemy at the other table.
          table[enemy] = not table[guest]
          stack.append(enemy)
        elif table[enemy] == table[guest]:
          print "No solution"
          return

def main():
  table = {}
  guests = {}
  with open("derpsons") as f:
    for guest,enemies in enumerate(f):
      guest = int(guest+1)
      enemies = [int(x) for x in enemies.split(",")]
      guests[guest] = enemies
      table[guest] = None

  depth_first(guests,table)
  table0,table1 = [],[]
  for v,k in table.items():
    if k: table0.append(v)
    else: table1.append(v)
  print table0
  print ""
  print table1
     

if __name__ == "__main__":
  main()
