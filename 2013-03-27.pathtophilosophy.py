#!/usr/bin/python
import requests,re

link = "http://en.wikipedia.org/w/api.php?action=query&prop=revisions|links&titles={}&rvprop=content&rvlimit=1&format=json&rvsection=0"
def path_to_philosophy(title):
  if title == "philosophy":
    return
  url = link.format(title)
  r = requests.get(url)
  j = r.json()
  page = j["query"]["pages"]
  text = page[page.keys()[0]]["revisions"][0]["*"]
  redirect = re.search(r"#REDIRECT \[\[(.*?)\]\]",text)
  if redirect:
    title = redirect.group(1)
  else: 
    title=re.search(r"\'{3}"+title+"\'{3}.*?\[\[(.*?)\]\]",text,flags=re.IGNORECASE).group(1)
  print title
  raw_input()
  path_to_philosophy(title)
  

if __name__ == "__main__":
  title = raw_input()
  path_to_philosophy(title)
