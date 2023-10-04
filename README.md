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
