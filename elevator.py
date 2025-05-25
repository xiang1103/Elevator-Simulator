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




# testing 
if __name__ == "__main__":
    my_elev= Elevator(2) 
    print(my_elev)
    for floor in my_elev.floors: 
        print(floor)

    