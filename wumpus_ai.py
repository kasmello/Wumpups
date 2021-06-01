from wumpus_engine import *

knowledge_base = {}

known_squares = {}


class square():
    #meaning of status: it is classified in numbers for the AI to sort through which ones to visit
    #   -1 = gold
    #   0 = never visited, but safe
    #   2 = safe, but visited
    #   4 = danger - hole
    #   6 = danger - wumpus
    #   if multiple sensed, numbers will be summed up
    #   difference of 2s so that AI will not be easily persuaded by gold

    def __init__(self,status=0,sensor=[],possibilities=[],obj=None):
        self.status=status
        self.sensor=sensor
        self.possibilities=possibilities
        self.obj=obj
        self.update_status()

    def update_status(self):
        for sense in self.sensor:
            if sense='glitter':
                self.status += -1
            elif sense='breeze':
                self.status += 4
            elif sense = 'smell':
                self.status += 6



class knowledge_sentence():
    def __init__(self,coords=[],sensed=[],sus_coords=[]):
        self.coords=coords
        self.sensed=sensed
        self.sus_coords=[]


def get_adj_squares(x,y): #returns adjacent squares and direction of those adjacent squares
    return_list = []
    if x-1 > -1:
        return_list.append([(x-1,y),'left'])
    if x+1 < 8:
        return_list.append([(x+1,y),'right'])
    if y-1 > -1:
        return_list.append([(x,y-1),'down'])
    if y+1 < 8:
        return_list.append([(x,y+1),'up'])
    return return_list

sensor_list = []

if __name__=='__main__':
    #first section is visualising move 0
    import os
    import time
    clear = lambda: os.system('cls')   

    def print_move():
        clear()
        print('\nWUMPUS WORLD - MOVE ' + str(no_moves) + '\n')
        visualise()
        time.sleep(0.5)

    print_move()
    
    
    while not finished:
        
        visit_list = []
        adj = get_adj_squares(player_pos_x,player_pos_y)        
            


        for item in adj:
            if known_squares.get(item[0]) == None:
                known_squares[item[0]] = square(sensor=sensor_list.copy()) #create new square class for that square
            else:
                known_squares[item[0]].sensor.extend(sensor_list)
                known_squares[item[0]].update_status()
            visit_list.append([known_squares[item[0]],item[1]) ## appends both the object and the direction of the object

    

        print_move()
        time.sleep(0.5)






