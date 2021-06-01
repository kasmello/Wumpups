
import numpy as np
import random


table = np.zeros(64, dtype='object').reshape(8,8) #each entry will be a list of all objects and smells
for i in range(8):
    for j in range(8):
        table[i,j] = [0]


# player will be defined as 1
# wumpus will be defined as 2
# wumpus' smell will be defined as 20
# exit will be defined as 3
# gold will be defined as 4
# glitter will be defined as 40
# hole will be defined as 5
# breeze will be defined as 50

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
                table[w_x+1,w_y].append(20)
            if w_x-1>-1:
                table[w_x-1,w_y].append(20)
            if w_y+1<8:
                table[w_x,w_y+1].append(20)
            if w_y-1>-1:
                table[w_x,w_y-1].append(20)



while h != no_hole:
    h_x = random.randint(0,7)
    h_y = random.randint(0,7)
    if table[h_x,h_y][0] == 0:
        if h_x+h_y>1 and h_x+h_y<13: #ensures holes do not block entrance or exit
            table[h_x,h_y][0] = 5
            h += 1
            if h_x+1<8:
                table[h_x+1,h_y].append(50)
            if h_x-1>-1:
                table[h_x-1,h_y].append(50)
            if h_y+1<8:
                table[h_x,h_y+1].append(50)
            if h_y-1>-1:
                table[h_x,h_y-1].append(50)


while g != no_gold:
    g_x = random.randint(0,7)
    g_y = random.randint(0,7)
    if table[g_x,g_y][0] == 0:
        table[g_x,g_y][0] = 4
        g += 1
        if g_x+1<8:
            table[g_x+1,g_y].append(40)
        if g_x-1>-1:
            table[g_x-1,g_y].append(40)
        if g_y+1<8:
            table[g_x,g_y+1].append(40)
        if g_y-1>-1:
            table[g_x,g_y-1].append(40)








if __name__ == "__main__": #if this module is chosen as main program
    import os

    clear = lambda: os.system('cls')

    def visualise():
        
       
        for row in table:
            for item in row:
                print(int(sum(item)),end='\t')
            print()
    clear()
    print('\nWUMPUS WORLD - TERMINAL\n')
    visualise()