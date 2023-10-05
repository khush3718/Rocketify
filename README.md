# Rocket Launch Simulator

This is a terminal based application that simulates a rocket launch that places a satellite into orbit, while providing real-time updates to the user. The simulator will operate in discrete time steps, each representing one second of the mission.

The Initial state for rocket: 

* Stage: "Pre-Launch"
* Fuel: 100%
* Altitude: 0 km
* Speed: 0 km/h

### User Input

    1. Pre-launch checks: User must type "start_checks" to initiate system checks.
    2. Launch: User types "launch" to begin the mission after checks are complete.
    3. Fast Forward : User types "fast_forward X" to advance the simulation by X seconds.

### Console Output (for example)

* Pre-launch checks: "All systems are ready. Initiate launch sequence to proceed."
* Each Second of Flight: "Stage: 1, Fuel: 90%, Altitude: 10 km, Speed: 1000 km/h"
* Stage Separation : "Stage 1 complete. Separating stage. Entering Stage 2."
* Orbit Placement: "Orbit achieved! Mission Successful."
* Mission Failure: "Rocket is out of fuel. Mission failed!!"

## Demo/Screenshots 

* To check if rocket is launched or not
  
![Screenshot 2023-10-05 102246](https://github.com/khush3718/Rocketify/assets/74204845/7010266a-9180-4828-8592-6bb069d2985d)

* launch the rocket
  
![Screenshot 2023-10-05 102309](https://github.com/khush3718/Rocketify/assets/74204845/5862368a-efa2-4c61-b855-dd05310e9a3f)

* fast forward the launch to when the stage seperation starts at altitude >= 1000km
  
![Screenshot 2023-10-05 102446](https://github.com/khush3718/Rocketify/assets/74204845/b67ced19-098a-4dd2-aaf1-bfb0dbd2c880)

* Successfully reached the orbit after reaching altittude >= 5000km
  
![Screenshot 2023-10-05 102641](https://github.com/khush3718/Rocketify/assets/74204845/99fbf4fd-a345-4ee9-bf16-84f2e7a25772)

