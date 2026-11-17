## Questions

### a. What is duck typing, as explained in the video?
Duck typing is another way to express and achieve polymorphism, apart from inheritance. Given objects must have the basic and minimum necessary attributes/methods.

### b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
The car class needed to have the equivalent method as the class of both Dog and Cat, as duck typing allows it to function inside the loop because it disregards what class it orginates from, only its function and if it satisfies the condition (possesses the same method).

---

## Python Source Code ('sg11_polymorphism_a2')

```python
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
```

---

### How does the code in 2.2 demonstrate polymorphism?
The code in 2.2 demonstrates polymorphism by utilizing the same method for each class while performing different actions, despite originationg from different classes. Due to that, it allows a signle function to to process objects of different types identically.