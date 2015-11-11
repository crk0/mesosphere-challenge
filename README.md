# mesosphere-challenge

Usage: > python main.py [-t]
The optional [-t] argument is used to enable the running of the basic test provided.

API
=======

ElevatorControlSystem():
	__init__(numElevators) # initialise the control system with 'numElevators' elevators
	pickup(floor, direction) # specify a pickup request at 'floor' with 'direction'
	step() # Step the simulation forward
	
	
The simulation step moves all elevators to their next goal floor. The goal floor is decided by
an algorithm that takes into consideration the direction the elevator is currently heading in 
and the other queued goal floors. 
The algorithm orders the goal floors in a way that minimises the number of trips required by 
the elevator to serve all the pickup requests.

A simple test is provided to show the order in which the pickup requests are executed is different
to the order they were specified. The expected order is tested against the actual order to confirm
whether the scheduler is correct.


