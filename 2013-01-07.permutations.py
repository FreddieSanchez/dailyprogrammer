import sys

def permute(s):
  permutations = []
  for i in range(len(s)):
    for j in range(len(s)):
       swaped = swap(i,j,s)
       if swaped not in permutations: 
         permutations.append(swaped)
  return permutations

def swap(c1, c2, s):
  s = bytearray(s)
  c = s[c1]
  s[c1] = s[c2]
  s[c2] = c
  return str(s)


def main():
  s = ["easy","baz","abbccc","foo"]
  for word in s:
    for p in permute(word):
      print p

  return

if __name__ == '__main__':
  main()
