#!/usr/bin/python
import os, sys, codecs

files = {"Portuguese":{"name":"br.dic","encoding":"UTF-16"},
         "German":{"name":"de_neu.dic","encoding":"UTF-16"},
         "French":{"name":"fr.dic","encoding":"UTF-16"},
         "English":{"name":"eng_com.dic","encoding":"ASCII"},
        "Spanish":{"name":"es.dic","encoding":"UTF-16"}
        }

# read words as unicode UTF-8 encoding. Remove any words with an apostrophe.
words = set([x for x in raw_input().decode('UTF-8').lower().split() if '\'' not in x])
lens = []


for language, file in files.items():
  if file['encoding'] == "ASCII":
    f = open(file['name'])
  else:
    f = codecs.open(file['name'],'r',file['encoding'])

  # Add all the words in the dictionary to a set.
  s = set()
  for line in f:
    w = line.lower().rstrip()
    s.add(w)
  f.close()
  
  # When you union the two sets, most of the words in the input should be in the dictionary
  # and it should not grow very much. Keep track of how much it grew by.
  new = s.union(words)
  lens.append([language,len(new) - len(s)])

# find the language that grew the set the least.
minimum = min(lens,key=lambda x: x[1])[1]      
for l in sorted(lens,key=lambda x: x[1]): # sort the differences, 
                                          # the language that it's most likely will be 
                                          # closer to the front of the list.
  if l[1] - minimum < .20 * len(words): # print the languages that grew the dictionary set
                                        # by less than 10%
    print l[0]

