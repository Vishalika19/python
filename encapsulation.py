class Car:
    # Class variable (same for all objects)
    brand = "Tesla"
    
    def __init__(self):
        self.speed = 0      # initial speed
        self.gear_no = 0    # initial gear
    
    def engineStart(self):
        print(f"{Car.brand} engine started.")
    
    def engineStop(self):
        print(f"{Car.brand} engine stopped.")
    
    def accelerate(self):
        if self.speed < 300:
            self.speed += 25
            if self.speed > 300:
                self.speed = 300
            print(f"Accelerating... Speed: {self.speed} kmph")
        if self.speed == 300:
            print("Max speed reached!")
    
    def brake(self):
        if self.speed > 0:
            self.speed -= 25
            if self.speed < 0:
                self.speed = 0
            print(f"Braking... Speed: {self.speed} kmph")
        else:
            print("Car is already stopped.")
    
    def suddenBrake(self):
        self.speed = 0
        print("Sudden brake applied! Speed: 0 kmph")
    
    def gear(self):
        if self.gear_no < 5:
            self.gear_no += 1
            print(f"Gear shifted to {self.gear_no}")
        else:
            print("Already in top gear (5).")
