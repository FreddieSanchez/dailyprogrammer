#!/usr/bin/python

import sys
WALL = "W"
PATH = "."
END = "E"
START = "S"

def readmap():
  mapsize = int(raw_input())
  unvisted = []
  map = [["" for x in range(mapsize)] for y in range(mapsize)]
  for row in range(mapsize):
    r = raw_input()
    for col in range(mapsize):
      map[row][col] = {"path":r[col], \
                       "visited":False,\
                       "distance":sys.maxint,\
                       "row":row,\
                       "col":col }
      if r[col] != WALL:
        unvisted.append(map[row][col])
      if r[col] == START:
        start = (row,col)
  return (map,unvisted,start)

def update_neighbor_distance(map,row,col,distance):
  if row < 0 or row >= len(map) or \
     col < 0 or col >= len(map) or \
     map[row][col]["visited"] or \
     map[row][col]["distance"] < distance:
    return
  map[row][col]["distance"] = distance + 1
        
def dijkstra(map,unvisted_set,row,col):
  
  map[row][col]['distance'] = 0
  while len(unvisted_set):
    unvisted_set = sorted(unvisted_set,key=lambda dist: dist['distance'])
    vertex = unvisted_set.pop(0)
    row = vertex['row']
    col = vertex['col']

    if vertex['distance'] == sys.maxint:
      break

    for (r,c) in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
      update_neighbor_distance(map,r,c,vertex['distance'])

    map[row][col]['visited'] = True

  return map

def path_exist(map,row,col):
  for r in range(len(map)):
    for c in range(len(map)):
      map[r][c]['visited'] = False

  while True:
    min = sys.maxint
    r1,c1 = row,col

    map[row][col]['visited'] = True
    for (r,c) in [(row-1,col),(row+1,col),(row,col-1),(row,col+1)]:
      if r < 0 or r >= len(map) or \
         c < 0 or c >= len(map) or \
         map[r][c]['visited']:
        continue
      if map[r][c]['distance'] < min:
        min = map[r][c]
        r1,c1 = r,c
    if r1 == row and c1 == col:
      print "False";
      break
    row,col = r1,c1
    if map[row][col]['path'] == END:
      print "True,",map[row][col]['distance']
      break

def main():
  (map,unvisited_set,start) = readmap()
  map = dijkstra(map,unvisited_set,start[0],start[1])
  path_exist(map,start[0],start[1]) 

if __name__ == "__main__":
  main()
