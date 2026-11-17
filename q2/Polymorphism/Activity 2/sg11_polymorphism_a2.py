class Car: # Define class Car
    def move(self):
        print("The car drives on the road.")

class Boat: # Define class of Boat
    def move(self):
        print("The boat sails on water.")

class Drone: # Define class drone
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle): # takes vehicle object and calls move method
    vehicle.move()

# instances for each class
car = Car()
boat = Boat()
drone = Drone()

# call start_trip function for each instance
start_trip(car)
start_trip(boat)
start_trip(drone)