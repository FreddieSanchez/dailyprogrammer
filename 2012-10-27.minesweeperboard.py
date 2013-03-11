import sys, random

MINE = "X"
def make_board(height,width,num_mines):
  board = [[0 for c in range(width)] for r in range(height)]
  mines = sorted(random.sample(range(width*height),num_mines))
  print mines
  for row in range(height):
    for col in range(width):
      if (row*width + col) in mines:
        board[row][col] = MINE
        board = increment_mine_count(row,col,board)
        continue 
  return board

def increment_mine_count(row,col,board):
  for r in range(row-1,row+2):
    if r >= 0 and r < len(board):
      for c in range(col-1,col+2):
        if c >=0 and c < len(board[r]) and board[r][c] != MINE:
          board[r][c] += 1
  return board

def main():
  height = 10; #int(raw_input("Height:"))
  width = 15 #int(raw_input("Width:"))
  mines = 20 #int(raw_input("Mines:"))
  for row in make_board(height,width,mines):
    print "[",
    for col in row:
      print col,
    print "]"
  return

if __name__ == "__main__":
  main()
