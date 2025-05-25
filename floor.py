
# floor object 

IDLE= "idle"    # floor did not make any calls 
AWAITING= "awaiting"    # awaiting elevator for pick up and drop off 

class Floor(): 
    def __init__(self, num:int): 
        self.status= IDLE 
        self.up= False 
        self.down= False 
        self.number= num 

    def __str__(self):
        return f"Floor: {self.number}"
    
    
    def set_status(self):
        ''' 
        Set the satus of the floor instance after call_up or call_down has been called 
        '''
        if (self.up or self.down):  # if either is true, the floor is awaiting elevator 
            self.status= AWAITING 
        else: 
            self.status= IDLE 
 
    def call_up(self): 
        ''' 
        Call to go up in the elevator 
        '''
        self.up= True 
        self.set_status() 


    def call_down (self):
        ''' 
        Call to come down in the elevator 
        '''
        self.down= True 
        self.set_status()  