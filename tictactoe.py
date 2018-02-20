'''game board'''
board = [0,1,2,
         3,4,5,
         6,7,8]
def bigboard():
    none = board[0]
    first = board[1]
    second = board[2]
    third = board[3]
    fourth = board[4]
    fifth = board[5]
    sixth = board[6]
    seventh = board[7]
    eigth = board[8]
    print("_____________")
    print (none,("   "), first,("   "), second)
    print("_____________")
    print (third,("   "), fourth, ("   "), fifth)
    print("_____________")
    print (sixth,("   "), seventh,("   "), eigth)
    
'''list Xs and Os'''
biglist = []
def checkplease1(player1):
    x = 0
    for x in range(len(biglist)):
        if int(biglist[int(x)]) == int(player1):
            return True
        x = x + 1
    
            
 
    
def checkplease2(player2):
    y = 0
    for y in range (len(biglist)):
        if int(biglist[int(y)]) == int(player2):
            return True
        y = y + 1



'''Instructions'''
def instructions():
    print("---------------------------------------")
    print("|      I N S T R U C T I O N S        |")
    print("---------------------------------------")
    print("|  Tic Tac Toe is a very basic game   |")
    print("|        number of players: 2         |")
    print("|                                     |")
    print("|   There is one board with 9 tiles   |")
    print("| Player 1 has Xs and Player 2 has Os |")
    print("|  The tiles are numbered so type in  |")
    print("|    the tile number that you want    |")
    print("|                                     |")
    print("| Objective: first to get 3 in a row  |")
    print("|                                     |")
    print("|         Some other Commands:        |")
    print("|                                     |")
    print("|  'q' is to quit out of this game    |")
    print("|  'c' is to come back to the         |")
    print("|      instructions page              |")
    print("|  's' is to start the game over      |")
    print("---------------------------------------")


    
'''Checking if 3 Xs or 3 Os for Player 2'''
def check2():
    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        print("player 2 wins!")
        return 
    if board[0] == "O" and board[4] == "O" and board[8] == "O":
        print("player 2 wins!")
        return
    if board[2] == "O" and board[4] == "O" and board[6] == "O":
        print("player 2 wins!")
        return
    if board[0] == "O" and board[1] == "O" and board[2] == "O":
        print("player 2 wins!")
        return
    if board[3] == "O" and board[4] == "O" and board[5] == "O":
        print("player 2 wins!")
        return
    if board[6] == "O" and board[7] == "O" and board[8] == "O":
        print("player 2 wins!")
        return
    if board[0] == "O" and board[3] == "O" and board[6] == "O":
        print("player 2 wins!")
        return
    if board[1] == "O" and board[4] == "O" and board[7] == "O":
        print("player 2 wins!")
        return
    if board[2] == "O" and board[5] == "O" and board[8] == "O":
        print("player 2 wins!")
        return
    if board[0] != 0 and board[1] != 1 and board[2] != 2 and board[3] != 3 and board[4] != 4 and board[5] != 5 and board[6] != 6 and board[7] != 7 and board[8] != 8:
        print("It's a Draw")
        return
        
        
    else:
        game1()

    
'''The game for player 2'''
def togame2():
    game2()
    
def game2():
    player2 = input("Player 2, where do you want your O? ")
    if player2 == ("q"):
        exit()
    if player2.isalpha():
        print("Thats not a number on the board")
        togame2()
    if int(player2) > 8:
        print("Thats not a number on the board")
        togame2()
    if int(player2) < 0:
        print("Thats not a number on the board")
        togame2()
    else:
        if checkplease2(player2) == True:    
            print("This spot is already taken")
            togame2()
        else:
            board[int(player2)] = "O"
            biglist.append(player2)
            bigboard()
            check2()
   
    
    
    
'''Checking if 3 Xs or 3 Os for Player 1'''
def check1():
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("player 1 wins!")
        return
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("player 1 wins!")
        return
    if board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("player 1 wins!")
        return
    if board[2] == "O" and board[4] == "O" and board[6] == "O":
        print("player 1 wins!")
        return
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("player 1 wins!")
        return
    if board[3] == "X" and board[4] == "X" and board[5] == "X":
        print("player 1 wins!")
        return
    if board[6] == "X" and board[7] == "X" and board[8] == "X":
        print("player 1 wins!")
        return
    if board[0] == "X" and board[3] == "X" and board[6] == "X":
        print("player 1 wins!")
        return
    if board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("player 1 wins!")
        return
    if board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("player 1 wins!")
        return
    if board[0] != 0 and board[1] != 1 and board[2] != 2 and board[3] != 3 and board[4] != 4 and board[5] != 5 and board[6] != 6 and board[7] != 7 and board[8] != 8:
        print("It's a Draw")
        return
    else:
        game2()

'''The Game for player 1'''
def togame1():
    game1()
    
def game1():
    player1 = input("Player 1, where do you want your X? ")
    if player1 == ("q"):
        exit()
    if player1.isalpha():
        print("Thats not a number on the board")
        togame1()
    if int(player1) > 8:
        print("Thats not a number on the board")
        togame1()
    if int(player1) < 0:
        print("Thats not a number on the board")
        togame1()
    else:
        if checkplease1(player1) == True:
            print("This spot is already taken")
            togame1()
        else:
            board[int(player1)] = "X"
            biglist.append(player1)
            bigboard()
            check1()
   
    
'''Beginning game'''


def tostart():
    start()
def start():
    print("----------------------------------------------------")
    print ("|           Hello welcome to Tic Tac Toe!          |")
    print("----------------------------------------------------")
    intro = input("{ Type 'start' to begin or 'c' for instructions} ")
    if intro == ("q"):
        exit()
    if intro == ("c"):
        instructions()
        tostart()
    if intro == "start":
        bigboard()
    if intro != "start":
        print("command not found")
        tostart()

start()

print ("player 1 is X and player 2 is O")
game1()


