#!/usr/bin/python

import sys,requests,re

URL = 'http://www.reddit.com/r/dailyprogrammer/.json?limit=none&after='
# output format
# [Easy / Medium / Hard] #<ID>: "<Title>" <URL>

# title format: 
# [01/21/13] Challenge #118 [Easy] Date Localization
# [easy] challenge #2
def format_title(title):
  m = re.search(r'\[easy.*\]|\[intermediate\]|\[difficult\]|\[hard\]',title,flags=re.IGNORECASE)

  difficulty = ""
  if m:
    difficulty = m.group()
    for x,y in [("easy","Easy"),("intermediate","Medium"),("difficult","hard")]:
      difficulty = re.sub(x,y,difficulty,flags=re.IGNORECASE)
    
  m = re.search(r'#\d*',title)

  number = ""
  if m:
    number = m.group()
  m = re.search(r'#\d*\s\[\w*\]\s(\w*.*$)',title)

  name = ""
  if m:
    name = m.group(1)

  return difficulty.title() + " " + number + " " + name

def get_posts():
  
  r = requests.get(URL)
  j = r.json()
  posts = j['data']['children']
  titles = []
  while True:
    for post in posts:
      title = post['data']['title']
      if "#" not in title:
        continue
      title = format_title(title) 
      url = post['data']['url']
      titles.append(title + " " + url)

    if j['data']['after'] == None:
          break
    r = requests.get(URL+j['data']['after'])
    j = r.json()
    posts = j['data']['children']
  return titles
  
def sort_level(post):
  first_word = (post.split())[0]
  second_word = (post.split())[1]
  return (first_word,second_word[1:])

#  if "Easy" in first_word:
#    return (0,second_word)
#  if "Medium" in first_word:
#    return (1,second_word)
#  if "Hard" in first_word:
#    return (2,second_word)
#  return 3

def sort_number(post):
  first_word = (post.split())[0]
  second_word = (post.split())[1]
  return (second_word[1:],first_word)
#  if "Easy" in first_word:
#    return (second_word,0)
#  if "Medium" in first_word:
#    return (second_word,1)
#  if "Hard" in first_word:
#    return (second_word,2)
#  return 3
#
def main():
  posts = get_posts()
  print "List One:"
  list1 = sorted(posts, key=sort_level)
  for post  in list1:
    print post
  print "List Two:"
  list1 = sorted(posts, key=sort_number)
  for post  in list1:
    print post
if __name__ == '__main__':
  main()
