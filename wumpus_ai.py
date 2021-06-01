from wumpus_engine import *

knowledge_base = [] #full of knowledge via senses

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

    def __init__(self,coord=[],status=0,sensor=[],possibilities=[],obj='Unknown'):
        self.coord=coord
        self.status=status
        self.sensor=sensor
        self.possibilities=possibilities
        self.obj=obj
        self.update_status()

    def update_status(self):
        for sense in self.sensor:
            if sense=='glitter':
                self.status += -1
            elif sense=='breeze':
                self.status += 4
            elif sense == 'smell':
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
        return_list.append([(x,y-1),'up'])
    if y+1 < 8:
        return_list.append([(x,y+1),'down'])
    return return_list

sensor_list = []

def print_adj(adj): #list of current adj squares
    adj_str = ''
    for item in adj:
        adj_str += str(item[0])+' - ' + known_squares[item[0]].obj
        if known_squares[item[0]].obj != 'Unknown':
            adj_str += ', Senses - '
            for senses in known_squares[item[0]].sensor:
                adj_str += senses +' '
        adj_str += '\n'
    return ('Adjacent squares:\n' + adj_str)

def print_prio(visit_list): #prints possible next moves in order of priority
    prio_str = ''
    for item in visit_list:
        prio_str += str(item[0].coord) + ' - ' + item[1] + ' (Priority Status = ' + str(item[0].status) + ')\n'
    return ('Move priority order:\n' + prio_str)


if __name__=='__main__':
    #first section is visualising move 0
    import os
    import time
    clear = lambda: os.system('cls')   

    def print_move():
        clear()
        print('\nWUMPUS WORLD - MOVE ' + str(no_moves) + '\n')
        visualise()
        

    
    
    while not finished:
        
        
        visit_list = []
        adj = get_adj_squares(player_pos_x,player_pos_y)        
            


        for item in adj:
            if known_squares.get(item[0]) == None:
                known_squares[item[0]] = square(coord = item[0],sensor=sensor_list.copy()) #create new square class for that square
            else:
                known_squares[item[0]].sensor.extend(sensor_list)
                known_squares[item[0]].update_status()
            visit_list.append([known_squares[item[0]],item[1]]) ## appends both the object and the direction of the object
        visit_list.sort(key = lambda x: x[0].status)
        
        finished = True

        print_move()
        print()
        print(print_adj(adj))
        print(print_prio(visit_list))
        time.sleep(0.5)
        make_move(visit_list[0][1])    
        






