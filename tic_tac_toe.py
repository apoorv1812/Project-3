class tic_tac_toe:
    def __init__(self):
        print("The game is starting....")
    def game_starting(self):
        self.player_1=input("Enter the name: ")
        self.player_2=input("Enter the name: ")
        while True:
            self.choice_1=input("Choose from O or X: ")
            self.choice_2=input("Choose from O or X: ")
            if self.choice_1 in ["O", "X"] and self.choice_2 in ["O", "X"]:
                break
            else:
                print("Enter again!")
                self.choice_1=input("Choose from O or X: ")
                self.choice_2=input("Choose from O or X: ")
    def game_moves(self):
        board1=[1,2,3]
        board2=[4,5,6]
        board3=[7,8,9]
        print(board1)
        print(board2)
        print(board3)
        if self.choice_1=="O":
                for items in board1, board2, board3=="O" and "X":
                    print(f"Play your move {self.player_1}")
                    self.moves_player1=int(input("Where do you want to play your move? "))
                    if self.moves_player1==1:
                        board1[0]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==2:
                        board1[1]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==3:
                        board1[2]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==4:
                        board2[0]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==5:
                        board2[1]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==6:
                        board2[2]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==7:
                        board3[0]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==8:
                        board2[1]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==9:
                        board3[2]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    print(f"Play your move {self.player_2}")
                    self.moves_player2=int(input("Where do you want to play your move? "))
                    if self.moves_player2==1:
                        board1[0]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==2:
                        board1[1]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==3:
                        board1[2]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==4:
                        board2[0]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==5:
                        board2[1]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==6:
                        board2[2]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==7:
                        board3[0]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==8:
                        board3[1]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==9:
                        board3[2]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
        elif self.choice_2=="O":
                for items in board1, board2, board3=="O" and "X":
                    print(f"Play your move {self.player_2}")
                    self.moves_player2=int(input("Where do you want to play your move? "))
                    if self.moves_player2==1:
                        board1[0]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==2:
                        board1[1]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==3:
                        board1[2]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==4:
                        board2[0]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==5:
                        board2[1]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==6:
                        board2[2]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==7:
                        board3[0]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==8:
                        board3[1]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player2==9:
                        board3[2]="O"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    print(f"Play your move {self.player_1}")
                    self.moves_player1=int(input("Where do you want to play your move? "))
                    if self.moves_player1==1:
                        board1[0]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==2:
                        board1[1]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==3:
                        board1[2]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==4:
                        board2[0]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==5:
                        board2[1]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==6:
                        board2[2]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==7:
                        board3[0]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==8:
                        board2[1]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                    elif self.moves_player1==9:
                        board3[2]="X"
                        print(board1)
                        print(board2)
                        print(board3)
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
                        if (board1[0] == self.choice_1 and board1[1] == self.choice_1 and board1[2] == self.choice_1) \
                        or (board2[0] == self.choice_1 and board2[1] == self.choice_1 and board2[2] == self.choice_1) \
                        or (board3[0] == self.choice_1 and board3[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[0] == self.choice_1 and board3[0] == self.choice_1) \
                        or (board1[1] == self.choice_1 and board2[1] == self.choice_1 and board3[1] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[2] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[0] == self.choice_1 and board2[1] == self.choice_1 and board3[2] == self.choice_1) \
                        or (board1[2] == self.choice_1 and board2[1] == self.choice_1 and board3[0] == self.choice_1):
                            print(f"The game is won by {self.player_1}")
                            break
game=tic_tac_toe()
game.game_starting()
game.game_moves()
        
        

        





        
        
        