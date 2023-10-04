
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
        
        print(f"Stage {self.stage} complete.Seperating stage. Engaging next stage. {int(self.stage) + 1}.")
        self.stage = str(int(self.stage) + 1)
        self._fuel = 100
        self.speed += 100

class Simulator:
    def __init__(self):
        self.rocket = Rocket()

    def start_checks(self):
        if self.rocket.stage == "pre-launch":
            print("All systems are ready. Initiate launch sequence to proceed.")
        else:
            print("Rocket is already in flight. Initiate stage seperation to proceed.")

    def launch_sequence(self):
        if self.rocket.stage == "pre-launch":
            print("Initiating launch sequence.")
            self.rocket.stage = "1"
            print("Launch sequence complete. Rocket is in flight.")
        else:
            print("Rocket is already in flight. Initiate stage seperation to proceed.")

    def fast_forward(self,seconds):
        if self.rocket.stage == "pre-launch":
            print("Rocket is still on the launch pad. Initiate launch sequence to proceed.")
            return
        
        for _ in range(seconds):
            self.rocket.update(1)
            if self.rocket._altitude >= 10000:
                print("Orbit achieved. Mission success!!")
                break
            elif self.rocket._altitude >= 5000:
                self.rocket.stage_seperation()
                break

    def run_simulator(self):
        while True:
            user = input("Enter command: ")
            if user == "start_checks":
                self.start_checks()
            elif user == "launch":
                self.launch_sequence()
            elif user.startswith("fast_forward"):
                try:
                    seconds = int(user.split(" ")[1])
                    self.fast_forward(seconds)
                except ValueError:
                    print("Invalid input. Use 'fast_forward S' where S is an integer.")
            else:
                print("Invalid command. Please enter 'start_checks', 'launch', or 'fast_forward S.")


if __name__ == "__main__":
    simulator = Simulator()
    simulator.run_simulator()