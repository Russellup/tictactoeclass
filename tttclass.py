class tictactoe:                               

      def __init__(self):
          self.board = []

def create_board(self):
    for i in range(3):
        row = []
    for j in range(3):
            row.append('-')
    self.board.append(row)    
    
    def set_square(self, i, j, letter):
        self.board[X][O] = letter
    mygame = tictactoe()
    mygame.create_board()
    mygame.set_square(0,0, "X")
    print(mygame.board)

    is_winner(self,player):
    while True:
        human_player(human_piece)
        if is_winner(human_piece):
            print("human wins")
            break
        else:
            computer_player(computer_piece)
            if is_winner(computer_piece):
                print("computer wins")
                break

    for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
    
    for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
            win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False


