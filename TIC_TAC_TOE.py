'''
INTRO : GAME OF TIC-TACC-TOE INCLUDING BOTH SINGLE PLAYER AND DOUBLE PLAYER MODES

SINGLE PLAYER MODE :

    HOW TO PLAY : -> YOU SEE TWO 3X3 GRIDS ON THE SCREEN
                  -> YOU GET X AND THE COMPUTER GETS O
                  -> YOU PUT ON YOUR X MARK BY TYPING ON THE CORRESPONDING
                     NUMBER FOUND ON THE SECOND GRID


    RULES : -> THE FIRST PLAYER TO GET THREE OF THEIR MARKS IN A
               ROW (UP,DOWN,ACROSS,DIAGONALLY) WINS THE GAME
            -> WHEN ALL 9 SQUARES ARE FULL AND NO PLAYER HAS 3 MARKS IN A ROW,
               THE GAME ENDS IN A DRAW

DOUBLE PLAYER MODE :

    HOW TO PLAY : -> YOU SEE TWO 3X3 GRIDS ON THE SCREEN
                  -> THE FIRST PLAYER GETS X AND SECOND PLAYER GETS O
                  -> PLAYER PUTS ON THEIR MARK BY TYPING THE CORRESPONDING
                     NUMBER FOUND ON THE SECOND GRID


    RULES : -> THE FIRST PLAYER TO GET THREE OF THEIR MARKS IN A
               ROW (UP,DOWN,ACROSS,DIAGONALLY) WINS THE GAME
            -> WHEN ALL 9 SQUARES ARE FULL AND NO PLAYER HAS 3 MARKS IN A ROW,
               THE GAME ENDS IN A DRAW


'''

import pygame
import random
pygame.init()
gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('Tic Tac Toe')
black=(0,0,0) #color-black
green=(0,255,0) #color-green
red=(255,0,0) #color-red
gameQuit=False
font=pygame.font.SysFont(None,50)


def msg_on_screen(msg, coordinates):
    screen_txt=font.render(msg, True, red)
    gameDisplay.blit(screen_txt, coordinates)

def display(type_of_game=''):
    gameDisplay.fill(black)
    #horizontal-line1
    pygame.draw.rect(gameDisplay,green,[460,100,5,200])
    pygame.draw.rect(gameDisplay,green,[540,100,5,200])
    #vertical-lin1
    pygame.draw.rect(gameDisplay,green,[400,166,200,5])
    pygame.draw.rect(gameDisplay,green,[400,232,200,5])
    #horizantal-line2
    pygame.draw.rect(gameDisplay,green,[200,100,5,200])
    pygame.draw.rect(gameDisplay,green,[280,100,5,200])
    #vertical-line2
    pygame.draw.rect(gameDisplay,green,[140,166,200,5])
    pygame.draw.rect(gameDisplay,green,[140,232,200,5])
    msg_on_screen('1', [420,125])
    msg_on_screen('2', [500,125])
    msg_on_screen('3', [580,125])
    msg_on_screen('4', [420,191])
    msg_on_screen('5', [500,191])
    msg_on_screen('6', [580,191])
    msg_on_screen('7', [420,256])
    msg_on_screen('8', [500,256])
    msg_on_screen('9', [580,256])
    if (type_of_game=='singleplayer'):
        msg_on_screen('YOU PLAY X AND GO FIRST', [20,400])
    elif (type_of_game=='doubleplayer'):
        msg_on_screen('FIRST PLAYER PLAYS X AND SECOND PLAYER PLAYS O', [20,400])
        
    pygame.display.update()

def singleplayer():
    display('singleplayer')

    gameOver=False
    key1=0 
    key2=0
    key3=0
    key4=0
    key5=0
    key6=0
    key7=0
    key8=0
    key9=0

    chance=0 #chance of player if chance=0 and computer's chance if chance=1
    
    xho1=0
    xho2=0
    xho3=0
    xve1=0
    xve2=0
    xve3=0
    xdia1=0
    xdia2=0

    oho1=0
    oho2=0
    oho3=0
    ove1=0
    ove2=0
    ove3=0
    odia1=0
    odia2=0
    
    draw=0

    while gameOver==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameOver=True
                gameQuit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    singleplayer()
                if event.key==pygame.K_q:
                    gameOver=True
                    gameQuit=True
                if chance==0:
                    if event.key==pygame.K_1:
                        if key1==0:
                            msg_on_screen('X', [160,125])
                            xho1+=1
                            xve1+=1
                            xdia1+=1
                            draw+=1
                            chance=1
                            key1=1
                    elif event.key==pygame.K_2:
                        if key2==0:
                            msg_on_screen('X', [240,125])
                            xho1+=1
                            xve2+=1
                            draw+=1
                            chance=1
                            key2=1
                    elif event.key==pygame.K_3:
                        if key3==0:
                            msg_on_screen('X', [310,125])
                            xdia2+=1
                            xho1+=1
                            xve3+=1
                            draw+=1
                            chance=1
                            key3=1
                    elif event.key==pygame.K_4:
                        if key4==0:
                            msg_on_screen('X', [160,191])
                            xho2+=1
                            xve1+=1
                            chance=1
                            draw+=1
                            key4=1
                    elif event.key==pygame.K_5:
                        if key5==0:
                            msg_on_screen('X', [240,191])
                            xdia2+=1
                            xho2+=1
                            xve2+=1
                            xdia1+=1
                            chance=1
                            draw+=1
                            key5=1
                    elif event.key==pygame.K_6:
                        if key6==0:
                            msg_on_screen('X', [310,191])
                            xho2+=1
                            xve3+=1
                            chance=1
                            draw+=1
                            key6=1
                    elif event.key==pygame.K_7:
                        if key7==0:
                            msg_on_screen('X', [160,256])
                            xho3+=1
                            xve1+=1
                            xdia2+=1
                            chance=1
                            draw+=1
                            key7=1
                    elif event.key==pygame.K_8:
                        if key8==0:
                            msg_on_screen('X', [240,256])
                            xho3+=1
                            xve2+=1
                            chance=1
                            draw+=1
                            key8=1
                    elif event.key==pygame.K_9:
                        if key9==0:
                            msg_on_screen('X', [310,256])
                            xho3+=1
                            xve3+=1
                            xdia1+=1
                            chance=1
                            draw+=1
                            key9=1

                while chance!=0 and draw!=9:
                    compx=random.choice([160,240,310])
                    compy=random.choice([191,256,125])
                        
                    if compx==160 and compy==125:
                        if key1==0:
                            msg_on_screen('O', [160,125])
                            oho1+=1
                            ove1+=1
                            odia1+=1
                            chance=0
                            draw+=1
                            key1=1
                        else:
                            continue
                    elif compx==240 and compy==125:
                        if key2==0:
                            msg_on_screen('O', [240,125])
                            oho1+=1
                            ove2+=1
                            chance=0
                            draw+=1
                            key2=1
                        else:
                            continue
                    elif compx==310 and compy==125:
                        if key3==0: 
                            msg_on_screen('O', [310,125])
                            odia2+=1
                            oho1+=1
                            ove3+=1
                            draw+=1
                            chance=0
                            key3=1
                        else:
                            continue
                    elif compx==160 and compy==191:
                        if key4==0:
                            msg_on_screen('O', [160,191])
                            oho2+=1
                            ove1+=1
                            chance=0
                            draw+=1
                            key4=1
                        else:
                            continue
                    elif compx==240 and compy==191:
                        if key5==0:
                            msg_on_screen('O', [240,191])
                            odia2+=1
                            oho2+=1
                            ove2+=1
                            odia1+=1
                            chance=0
                            draw+=1
                            key5=1
                        else:
                            continue
                    elif compx==310 and compy==191:
                        if key6==0:
                            msg_on_screen('O', [310,191])
                            oho2+=1
                            ove3+=1
                            chance=0
                            draw+=1
                            key6=1
                        else:
                            continue
                    elif compx==160 and compy==256:
                        if key7==0:
                            msg_on_screen('O', [160,256])
                            oho3+=1
                            ove1+=1
                            chance=0
                            draw+=1
                            key7=1
                        else:
                            continue
                    elif compx==240 and compy==256:
                        if key8==0:
                            msg_on_screen('O', [240,256])
                            oho3+=1
                            ove2+=1
                            chance=0
                            draw+=1
                            key8=1
                        else:
                            continue
                    elif compx==310 and compy==256:
                        if key9==0:
                            msg_on_screen('O', [310,256])
                            oho3+=1
                            ove3+=1
                            odia1+=1
                            chance=0
                            draw+=1
                            key9=1
                        else:
                            continue

        pygame.display.update()
                    
        if xho1==3 or xho2==3 or xho3==3 or xve1==3 or xve2==3 or xve3==3 or xdia1==3 or xdia2==3:
            msg_on_screen('X wins', [250,450])
            msg_on_screen('To play again press p', [250,500])
            msg_on_screen('To quit, press q', [250,550])
            pygame.display.update()
        elif oho1==3 or oho2==3 or oho3==3 or ove1==3 or ove2==3 or ove3==3 or odia1==3 or odia2==3:
            msg_on_screen('O wins', [250,450])
            msg_on_screen('To play again press p', [250,500])
            msg_on_screen('To quit, press q', [250,550])
            pygame.display.update()                
        elif draw==9:
            msg_on_screen('MATCH DRAW', [250,450])
            msg_on_screen('To play again press p', [250,500])
            msg_on_screen('To quit, press q', [250,550])
            pygame.display.update()

def doubleplayer():
    display('doubleplayer')

    gameOver=False
    key1=0 
    key2=0
    key3=0
    key4=0
    key5=0
    key6=0
    key7=0
    key8=0
    key9=0
    
    chance=0 #chance of player if chance=0 and computer's chance if chance=1
    
    xho1=0
    xho2=0
    xho3=0
    xve1=0
    xve2=0
    xve3=0
    xdia1=0
    xdia2=0

    oho1=0
    oho2=0
    oho3=0
    ove1=0
    ove2=0
    ove3=0
    odia1=0
    odia2=0
    
    draw=0

    while gameOver==False:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameOver=True
                gameQuit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p:
                    singleplayer()
                if event.key==pygame.K_q:
                    gameOver=True
                    gameQuit=True
                if chance==0:
                    if event.key==pygame.K_1:
                        if key1==0:
                            msg_on_screen('X', [160,125])
                            xho1+=1
                            xve1+=1
                            xdia1+=1
                            draw+=1
                            chance=1
                            key1=1
                    elif event.key==pygame.K_2:
                        if key2==0:
                            msg_on_screen('X', [240,125])
                            xho1+=1
                            xve2+=1
                            draw+=1
                            chance=1
                            key2=1
                    elif event.key==pygame.K_3:
                        if key3==0:
                            msg_on_screen('X', [310,125])
                            xdia2+=1
                            xho1+=1
                            xve3+=1
                            draw+=1
                            chance=1
                            key3=1
                    elif event.key==pygame.K_4:
                        if key4==0:
                            msg_on_screen('X', [160,191])
                            xho2+=1
                            xve1+=1
                            chance=1
                            draw+=1
                            key4=1
                    elif event.key==pygame.K_5:
                        if key5==0:
                            msg_on_screen('X', [240,191])
                            xdia2+=1
                            xho2+=1
                            xve2+=1
                            xdia1+=1
                            chance=1
                            draw+=1
                            key5=1
                    elif event.key==pygame.K_6:
                        if key6==0:
                            msg_on_screen('X', [310,191])
                            xho2+=1
                            xve3+=1
                            chance=1
                            draw+=1
                            key6=1
                    elif event.key==pygame.K_7:
                        if key7==0:
                            msg_on_screen('X', [160,256])
                            xho3+=1
                            xve1+=1
                            xdia2+=1
                            chance=1
                            draw+=1
                            key7=1
                    elif event.key==pygame.K_8:
                        if key8==0:
                            msg_on_screen('X', [240,256])
                            xho3+=1
                            xve2+=1
                            chance=1
                            draw+=1
                            key8=1
                    elif event.key==pygame.K_9:
                        if key9==0:
                            msg_on_screen('X', [310,256])
                            xho3+=1
                            xve3+=1
                            xdia1+=1
                            chance=1
                            draw+=1
                            key9=1

                if chance==1:
                    if event.key==pygame.K_1:
                        if key1==0:
                            msg_on_screen('O', [160,125])
                            oho1+=1
                            ove1+=1
                            odia1+=1
                            chance=0
                            draw+=1
                            key1=1
                        else:
                            continue
                    elif event.key==pygame.K_2:
                        if key2==0:
                            msg_on_screen('O', [240,125])
                            oho1+=1
                            ove2+=1
                            chance=0
                            draw+=1
                            key2=1
                        else:
                            continue
                    elif event.key==pygame.K_3:
                        if key3==0: 
                            msg_on_screen('O', [310,125])
                            odia2+=1
                            oho1+=1
                            ove3+=1
                            draw+=1
                            chance=0
                            key3=1
                        else:
                            continue
                    elif event.key==pygame.K_4:
                        if key4==0:
                            msg_on_screen('O', [160,191])
                            oho2+=1
                            ove1+=1
                            chance=0
                            draw+=1
                            key4=1
                        else:
                            continue
                    elif event.key==pygame.K_5:
                        if key5==0:
                            msg_on_screen('O', [240,191])
                            odia2+=1
                            oho2+=1
                            ove2+=1
                            odia1+=1
                            chance=0
                            draw+=1
                            key5=1
                        else:
                            continue
                    elif event.key==pygame.K_6:
                        if key6==0:
                            msg_on_screen('O', [310,191])
                            oho2+=1
                            ove3+=1
                            chance=0
                            draw+=1
                            key6=1
                        else:
                            continue
                    elif event.key==pygame.K_7:
                        if key7==0:
                            msg_on_screen('O', [160,256])
                            oho3+=1
                            ove1+=1
                            chance=0
                            draw+=1
                            key7=1
                        else:
                            continue
                    elif event.key==pygame.K_8:
                        if key8==0:
                            msg_on_screen('O', [240,256])
                            oho3+=1
                            ove2+=1
                            chance=0
                            draw+=1
                            key8=1
                        else:
                            continue
                    elif event.key==pygame.K_9:
                        if key9==0:
                            msg_on_screen('O', [310,256])
                            oho3+=1
                            ove3+=1
                            odia1+=1
                            chance=0
                            draw+=1
                            key9=1
                        else:
                            continue

        pygame.display.update()
                    
        if xho1==3 or xho2==3 or xho3==3 or xve1==3 or xve2==3 or xve3==3 or xdia1==3 or xdia2==3:
            msg_on_screen('X wins', [250,450])
            msg_on_screen('To play again press p', [250,500])
            msg_on_screen('To quit, press q', [250,550])
            pygame.display.update()
        elif oho1==3 or oho2==3 or oho3==3 or ove1==3 or ove2==3 or ove3==3 or odia1==3 or odia2==3:
            msg_on_screen('O wins', [250,450])
            msg_on_screen('To play again press p', [250,500])
            msg_on_screen('To quit, press q', [250,550])
            pygame.display.update()                
        elif draw==9:
            msg_on_screen('MATCH DRAW', [250,450])
            msg_on_screen('To play again press p', [250,500])
            msg_on_screen('To quit, press q', [250,550])
            pygame.display.update()


msg_on_screen('WELCOME TO TIC TAC TOE', [150,100])
msg_on_screen('To Start playing double player press d',[100,350])
msg_on_screen('To play against computer press s', [100,400])
msg_on_screen('To quit press q', [100,450])
pygame.display.update()

while gameQuit==False:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameQuit=True
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_q:
                gameQuit=True
            elif event.key==pygame.K_s:
                singleplayer()
            elif event.key==pygame.K_d:
                doubleplayer()
            else:
                continue

pygame.quit()
quit



