# Base class
class Animal:
    # Constructor
    def __init__(self, name, age, habitat):
        self.name = name
        self.age =age
        self.habitat = habitat
        self.available = True
    
    # method to mark as available
    def mark_as_available(self):
        self.available = True
    def mark_as_quarantine(self):
        self.available = False
    
    def display(self):
        print(f"Animal Name: {self.name}")
        print(f"Animal Age: {self.age}")
        print(f"Animal Habitat: {self.habitat}")
        status = "Yes" if self.available else "In Quarantine"
        print(f"Is {self.name} available to be viewed? {status}")
        
class Mammal(Animal):
    def __init__(self, name, age, habitat, fur_length, diet_type):
        super().__init__(name, age, habitat)
        self.fur_length = fur_length
        self.diet_type = diet_type
    
    def display(self):
        super().display()
        print(f"Fur Length: {self.fur_length}")
        print(f"Diet Type: {self.diet_type}")

class Bird(Animal):
    def __init__(self, name, age, habitat, wingspan, flight_altitude):
        super().__init__(name, age, habitat)
        self.wingspan = wingspan
        self.flight_altitude = flight_altitude
    
    def display(self):
        super().display()
        print(f"Wing Span: {self.wingspan}")
        print(f"Flight Altitude: {self.flight_altitude}")

class Reptile(Animal):
    def __init__(self, name, age, habitat, scale_pattern, venomous_status):
        super().__init__(name, age, habitat)
        self.scale_pattern = scale_pattern
        self.venomous_status = venomous_status
    
    def display(self):
        super().display()
        print(f"Scale Pattern: {self.scale_pattern}")
        print(f"Venomous Status: {self.venomous_status}")


mammal = Mammal("Elephant", 10, "Savannah", 2.5, "Herbivore")
bird = Bird("Eagle", 5, "Mountain", 2.0, 3000)
reptile = Reptile("Cobra", 3, "Rainforest", "striped", "Venomous")

print("Before Changing Availability Status:")
print("\n")
mammal.display()
print("\n")
bird.display()
print("\n")
reptile.display()

print("\nAfter Changing Availability Status:")
bird.mark_as_quarantine()
mammal.mark_as_available()
reptile.mark_as_quarantine()

mammal.display()
print("\n")
bird.display()
print("\n")
reptile.display()