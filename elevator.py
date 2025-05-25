from enum import Enum 

# final variables for elevator status 
UP= "up"
DOWN= "down"
IDLE = "idle"

class Elevator(): 
    def __init__(self, num_floor:int): 
        self.num_floor= num_floor # number of floors in this elevator 
        self.status= IDLE
        self.current_floor= -2  # default floor 


    @classmethod 
    def call_up(cls): 
        ''' 
        Call to go up in the elevator 
        '''
        pass  

    @classmethod 
    def call_down (cls):
        ''' 
        Call to come down in the elevator 
        '''
        pass 