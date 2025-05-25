from floor import Floor

# final variables for elevator status 
UP= "up"
DOWN= "down"
IDLE = "idle"

class Elevator(): 
    def __init__(self, num_floor:int): 
        self.num_floor= num_floor # number of floors in this elevator 
        self.status= IDLE
        self.current_floor= -2  # default floor 
        self.floors= self.make_floors() 


    def make_floors(self):
        ''' 
        Make the floors as array of floors 
        '''
        output= [] 
        for i in range(0,self.num_floor): 
            output.append(Floor(i))
        return output 

    def __str__(self):
        return f"Elevator in {self.status}. Total num floors: {self.num_floor}"

    def drop_off(self): 
        '''  
        pick up the floors that require pick up 
        '''
        for floor in self.floors: 
            if (floor.up): 
                floor.up= False 
                floor.set_status() 
    
    def pick_up(self): 
        for floor in self.floors: 
            if (floor.down): 
                floor.down= False 
                floor.set_status() 



# testing 
if __name__ == "__main__":
    my_elev= Elevator(2) 
    print(my_elev)
    for floor in my_elev.floors: 
        print(floor)

    