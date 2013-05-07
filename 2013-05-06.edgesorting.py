#!/usr/bin/python

    def main():
      num_edges = int(raw_input())
      edges_dict = {}
      while num_edges > 0:
        edges = raw_input().split()
        edges_dict[edges[0]] = edges[1:]
        num_edges -= 1
      print sorted(edges_dict, key=lambda key: (edges_dict[key][0],edges_dict[key][1]))


    if __name__ == "__main__":
      main()
