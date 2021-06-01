
import numpy as np
import random


table = np.zeros(64, dtype='object').reshape(8,8) #each entry will be a list of all objects and smells
for i in range(8):
    for j in range(8):
        table[i,j] = [0]


# player will be defined as 1
# wumpus will be defined as 2
# wumpus' smell will be defined as 'smell'
# exit will be defined as 3
# gold will be defined as 4
# glitter will be defined as 'glitter'
# hole will be defined as 5
# breeze will be defined as 'breeze'

player_pos_x = 0
player_pos_y = 0
table[player_pos_x,player_pos_y][0] = 1

exit_x = 7
exit_y = 7
table[exit_x,exit_y][0] = 3

#global variables:
no_wumpus = 1 #number of wumpuses
no_hole = 3 #number of holes
no_gold = 4 #number of gold




#randomization & creation of the table


w = h = g = 0
while w != no_wumpus:
    w_x = random.randint(0,7)
    w_y = random.randint(0,7)
    if (table[w_x,w_y][0] == 0):
        if w_x+w_y>1 and w_x+w_y<13: #ensures the wumpus does not block entrance or exit
            table[w_x,w_y][0] = 2
            w += 1
            if w_x+1<8:
                table[w_x+1,w_y].append('smell')
            if w_x-1>-1:
                table[w_x-1,w_y].append('smell')
            if w_y+1<8:
                table[w_x,w_y+1].append('smell')
            if w_y-1>-1:
                table[w_x,w_y-1].append('smell')



while h != no_hole:
    h_x = random.randint(0,7)
    h_y = random.randint(0,7)
    if table[h_x,h_y][0] == 0:
        if h_x+h_y>1 and h_x+h_y<13: #ensures holes do not block entrance or exit
            table[h_x,h_y][0] = 5
            h += 1
            if h_x+1<8:
                table[h_x+1,h_y].append('breeze')
            if h_x-1>-1:
                table[h_x-1,h_y].append('breeze')
            if h_y+1<8:
                table[h_x,h_y+1].append('breeze')
            if h_y-1>-1:
                table[h_x,h_y-1].append('breeze')


while g != no_gold:
    g_x = random.randint(0,7)
    g_y = random.randint(0,7)
    if table[g_x,g_y][0] == 0:
        if g_x+g_y>1 and g_x+g_y<13: #ensure gold does not spawn at entrance or exit
            table[g_x,g_y][0] = 4
            g += 1
            if g_x+1<8:
                table[g_x+1,g_y].append('glitter')
            if g_x-1>-1:
                table[g_x-1,g_y].append('glitter')
            if g_y+1<8:
                table[g_x,g_y+1].append('glitter')
            if g_y-1>-1:
                table[g_x,g_y-1].append('glitter')


#making the rules here
no_moves = 0
score = 0 #-10 for every move, +150 for gold found, +1000 for finishing
finished = False

def make_move(move): #moving the player right, left, up, down

    found = None #this variable returns what is found in the next square
    senses = [] #this variable returns the senses found in the next square
    if move == 'up' and player_pos_y+1<8:
        table[player_pos_x,player_pos_y][0] = 0
        player_pos_y += 1
    elif move == 'down' and player_pos_y-1>-1:
        table[player_pos_x,player_pos_y][0] = 0
        player_pos_y -= 1
    elif move == 'right' and player_pos_x+1<8:
        table[player_pos_x,player_pos_y][0] = 0
        player_pos_x += 1
    elif move == 'left' and player_pos_x-1>-1:
        table[player_pos_x,player_pos_y][0] = 0
        player_pos_x -= 1

    #if player hits gold:
    if table[player_pos_x,player_pos_y][0] == 4:
        score += 100
        found = 'gold'
    elif table[player_pos_x,player_pos_y][0] == 3:
        found = 'exit'
        score += 1000
        finished = True
    elif table[player_pos_x,player_pos_y][0] == 5:
        found = 'hole'
        finished = True
    elif table[player_pos_x,player_pos_y][0] == 2:
        found = 'wumpus'
        score -= 1000
        finished = True
    else:
        score -= 10
        senses.append(table[player_pos_x,player_pos_y][1:])





    no_moves += 1

    return found



def visualise():
        
       
        for row in table:
            for item in row:
                print(int(item[0]),end='\t')
            print()







if __name__ == "__main__": #if this module is chosen as main program
    import os

    clear = lambda: os.system('cls')

    
    clear()
    print('\nWUMPUS WORLD - INITIALIZE\n')
    visualise()