
class Rocket:
    def __init__(self):
        self.stage = "pre-launch"
        self._fuel = 100
        self._altitude = 0
        self.speed = 0


    def update(self,seconds):
        if self.stage == "pre-launch":
            print("Rocket is still on the launch pad. Initiate launch sequence to proceed.")
            return

        if self._fuel <= 0:
            print("Rocket is out of fuel. Mission failed!!")
            return 
        
        self._altitude += self.speed * seconds # update altitude based on speed
        self._fuel -= seconds # burn fuel
        print(f"Stage: {self.stage},Fuel: {self._fuel}%, Altitude: {self._altitude} km, Speed: {self.speed} km/hr")

    def stage_seperation(self):
        if self.stage == "pre-launch":
            print("Rocket is still on the launch pad. Initiate launch sequence to proceed.")
            return
        
        