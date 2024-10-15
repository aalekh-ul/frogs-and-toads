#frogs and toads game by aalekh
board =  ['F','F','F',' ','T','T','T']
index =  ["1","2","3","4","5","6","7"]
win = ['T','T','T',' ','F','F','F']
c = 0

def print_board():
    print(board)
    print(index)
    
def check_win():
    if board == win:
        return True
    


def game():
    global c
    while True:
        print_board()
        if check_win()== True:
            print(f"\n you won in {c} moves :) huooahh")
            break
        while True:
            pos = int(input("\nenter position: "))
            if pos > (len(board)) or pos <= 0:
                print(f"\nenter value between 1 - {len(board)}")
            else:
                break
        while True:
            dst = int(input("\nenter destination: "))
            if dst > (len(board)) or dst <= 0:
                print(f"\n enter value between 1 - {len(board)}")
            else:
                if dst > (pos+2) or dst < (pos-2):
                    print("\n you can't jump more than two spaces")
                else:
                    if (board[pos-1] == 'F' and pos > dst) or (board[pos-1] == 'T' and pos < dst):
                        print('\n you cant go backwards')
                    else:
                        break
       
        if board[dst-1] == ' ':
            board[dst-1] = board[pos-1]
            board[pos-1] = " "
            c = c + 1
        else:
            print("\ncant move to that position, already occupied")
        
game()
