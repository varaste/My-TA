import random

# -------------Setting the board, players and hiding battleships-------------

board = []

for x in range(0,5):
  board.append(["o"] * 5)

def print_board(board):
  for row in board:
    print (" ".join(row))

print("Let's play Battleship!")
print("This is a 2 player game")

player_1 = input("Enter first name: ")
player_2 = input("Enter second name: ")
players = [player_1, player_2]

def random_player(players):
    return random.choice(players)

def random_row(board):
  return random.randint(0,len(board)-1)

def random_col(board):
  return random.randint(0,len(board[0])-1)

if random_player(players) == player_1:
  print(player_1, "starts the game.")
else:
  print(player_2, "starts the game.")
  
ship_row_1 = random_row(board)
ship_col_1 = random_col(board)
# print (ship_row_1)
# print (ship_col_1)

ship_row_2 = random_row(board)
ship_col_2 = random_col(board)
# print (ship_row_2)
# print (ship_col_2)

print_board(board)

player_start = random_player(players)
# ----------------------------Playing the game----------------------------



hit_count = 0

for turn in range(4):
     guess_row = int(input("Guess Row: (allowed values: 0-4) "))
     guess_col = int(input("Guess Col: (allowed values: 0-4) "))

     if (guess_row == ship_row_1 and guess_col == ship_col_1) or (guess_row == ship_row_2 and guess_col == ship_col_2):
            hit_count = hit_count + 1
            board[guess_row][guess_col] = "*"
            print ("Congratulations! ")
            if hit_count == 1:
                   print("You sunk first battleship!") 
            elif hit_count == 2:
                   print("You sunk second battleship! You win!")
                   print_board(board)
                   break
     else:
            if (guess_row < 0 or guess_row > 4)  or (guess_col < 0 or guess_col > 4):
                   print ("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                   print ("You guessed that one already.")
            else:
                 print ("You missed my battleship!")
                 board[guess_row][guess_col] = "X"
            print (turn + 1, "turn")
     print_board(board)
print ("Ship 1 is hidden:")    
print (ship_row_1)
print (ship_col_1)

print ("Ship 2 is hidden:")    
print (ship_row_2)
print (ship_col_2)
print (ship_col_2)