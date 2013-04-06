#!/usr/bin/python
import requests,re

link = "http://en.wikipedia.org/w/api.php?action=query&prop=revisions|links&titles={}&rvprop=content&rvlimit=1&format=json&redirects"

def request_wiki(title):
  text = ""
  while True:
    url = link.format(title)
    r = requests.get(url)
    j = r.json()
    page = j["query"]["pages"]
    text = page[page.keys()[0]]["revisions"][0]["*"]
    redirect = re.search(r"#REDIRECT \[\[(.*?)\]\]",text)
    if redirect:
      title = redirect.group(1)
    else: 
      break
  return title,text

def index_containing_sub(l,s):
  for i,str in enumerate(l):
    if s in str:
      return i
  return -1

dict = {}
def wikipeida_find_all_links(title):
  if title in dict.keys():
    return dict[title]
  title,text = request_wiki(title)
  text = re.sub(r'\(.*?\)',"",text) # remove any parens
  text = re.sub(r'\{{2}.*?\}{2}',"",text) # remove any parens
  paragraphs = [x.lower()for x in text.split("\n")]
  start_p = index_containing_sub(paragraphs,"'''"+title+"'''")
  text = "".join(paragraphs[start_p:])
  expression = r"\[\[(.*?)\]\]"
  links =[link.split("|")[0] for link in re.findall(expression,text)]
  dict[title] = links
  return links


def wikipedia_first_link(title):
  title,text = request_wiki(title)
  links = wikipeida_find_all_links(title)
  return links[0]

def path_to_article(title,end_article):
  while title != end_article:
    title = wikipedia_first_link(title)
    print title
  
if __name__ == "__main__":
  start = raw_input()
  end = raw_input()
  path_to_article(start,end)
