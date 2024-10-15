import pygame as p
from playsound import playsound
import time

# Initial game board setup
board = ['F','F','F','','T','T','T']
#positions = [[225, 300], [345, 300], [465, 300], [585, 300], [705, 300], [825, 300], [945, 300]]
leaf_index = [225, 345, 465, 585, 705, 825, 945]
leaf_index_1 = [225, 345, 465, 585, 705, 825, 945,1065]
win = ['T','T','T','','F','F','F']
checkwin = False
counter = 0
HEIGTH = 1280
WIDTH = 720
FPS = 60

# Loading and transforming images
frogs = p.transform.scale(p.image.load('images/frogs.png'), (80, 70))
toads = p.transform.scale(p.image.load('images/toads.png'), (100, 80))
leafs = p.transform.scale(p.image.load('images/leaf.png'), (140, 100))
background = p.image.load('images/background.jpg')
reset_img = p.transform.scale(p.image.load('images/reset.png'), (80, 80))


def reset_button(screen,x,y):
    """creating a reset button"""
    global clicked,board,counter
    rect = reset_img.get_rect()
    rect.topright = (x,y)
    screen.blit(reset_img,(rect.x,rect.y))
    pos = p.mouse.get_pos() #get the position of mouse 
    if rect.collidepoint(pos):
        if p.mouse.get_pressed()[0] == 1 and not clicked:
            clicked = True
            counter = 0
            checkwin = False
            board = ['F', 'F', 'F', '', 'T', 'T', 'T']
            playsound('sound/reset_sound.mp3')
            print("clicked")
    if p.mouse.get_pressed()[0] == 0:
        clicked = False
    #drawPieces(board, screen)
    

def checkWin():
    """check for win condition"""
    if board == win:
        checkwin = True
        return checkwin
        
def printLeaf(screen):
    """printing leafs on the screen"""
    for i in leaf_index:
        screen.blit(leafs, (i, 300))

def drawPieces(board, screen):
    """drawing items on board"""
    for i, item in enumerate(board):
        item_x = leaf_index[i] + 25
        item_y = 300
        if item == "F":
            screen.blit(frogs, (item_x, item_y))
        elif item == "T":
            screen.blit(toads, (item_x, item_y))

def gameFinish(screen):
        screen = p.display.set_mode((HEIGTH, WIDTH))
        p.display.set_caption("you won the game")
        clock = p.time.Clock()
        running = True
        global clicks
        clicks = list()
        #reset_button(screen,700,80)
        while running:
            antialias = True
            color = (255,0,0)
            text = f"Congratulations, you won in {counter} moves"
            font = p.font.Font(p.font.get_default_font(), 36)
            text = font.render(text, antialias, color)
            screen.blit(background,(0,0))
            screen.blit(text, (300, 300))

            for event in p.event.get():
                if event.type == p.QUIT:  # Looking for quit event
                    running = False
            p.display.update()
        p.quit()

def checkClosest(num,positions):
    """getting the exact destination of user click"""
    closest = min(positions, key=lambda x: abs(x-num))
    if positions.index(closest) == 0:
        return closest
    return closest - 120
    
def gameEngine(clicks,screen):
    """game engine"""
    global counter 
    temp = ""
    if clicks[0][1] and clicks[1][1]  in range(300,390):
        pos = clicks[0][0]
        dst = clicks[1][0]
        checker = checkClosest(dst,leaf_index_1)
        for k in range(len(leaf_index_1)-1):
            #checkWin(counter,screen)
            if pos in range(leaf_index_1[k],leaf_index_1[k+1]):
                temp = board[k]
                
                for i in range(len(leaf_index_1)-1):
                    if dst in range(leaf_index_1[i],leaf_index_1[i+1]):
                        if temp == "F":
                            print(checker)
                            print(k)
                            print(checker,board[i],k,i)
                            print(k,i)
                            if abs(leaf_index_1.index(checker) - k) <= 2 and board[i] == "" and pos<dst:
                                board[k] = ""
                                board[i] = "F"
                                print(board)
                                playsound('sound/frogs.mp3')
                                counter += 1
            
                        if temp == "T":
                            if abs(leaf_index[i]-dst) < 70:
                                checker = checkClosest(dst,leaf_index_1) + 120
                                #print(k,leaf_index.index(checker))
                            # print(checker,board[i],k)
                            # print(k,i)
                            if abs(leaf_index_1.index(checker) - k) <= 2 and board[i] == "" and pos>dst:
                                board[k] = ""
                                board[i] = "T"
                                print(board)
                                playsound('sound/frogs.mp3')
                                counter +=1 

               

        print(clicks)

def main():
    p.init()
    screen = p.display.set_mode((HEIGTH, WIDTH))
    p.display.set_caption("Game by Aalekh")
    clock = p.time.Clock()
    running = True
    global clicks
    clicks = list()
    while running:
        screen.blit(background, (0, 0))  # Main canvas background
        printLeaf(screen)
        reset_button(screen,700,80)
        if checkWin() == True:
            gameFinish(screen)
        else:
            drawPieces(board, screen)  # Draw the pieces on the screen
        
        for event in p.event.get():
            if event.type == p.QUIT:  # Looking for quit event
                running = False
            if event.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
                if pos[1] in range(300,390):
                    clicks.append(pos)
                    if len(clicks) == 2:
                        gameEngine(clicks,screen)
                        clicks = []
                else:
                    clicks = []
        p.display.update()
        clock.tick(FPS)

    p.quit()

main()
