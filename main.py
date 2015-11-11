class Elevator():
	def __init__(self, id, currentFloor=0):
		''' A new elevator having ID=id, current floor = 0 (ground floor)
			and no goal floors.
		'''
		self._id 			= id;
		self._currentFloor 	= currentFloor
		self._goalFloor 	= set()
		self._dir 			= 0

	def status(self):
		''' Return triple representing state of elevator,
			state(id, current_floor, goal_floor)
		'''
		return (self._id, self._currentFloor, self._goalFloor)

	def update(self, currentFloor, goalFloors):
		''' Update the state of the elevator
		'''
		# update current floor
		self._currentFloor = currentFloor

		# remove currentFloor from goalFloor if it exists
		if currentFloor in self._goalFloor:
			self._goalFloor.remove(currentFloor)

		# add the new goal floors
		self._goalFloor.union(set(goalFloors))

class ElevatorControlSystem():
	def __init__(self, numElevators):
		# initialise numElevators instances of Elevator()
		self._elevators 	 = [Elevator(id) for id in range(0,numElevators)]
		self._pickupRequests = set()

	def status(self):
		''' Return a list of all states of the elevators 
		'''
		return [elevator.status() for elevator in self._elevators]

	def update(self, id, currentFloor, goalFloors):
		''' Update the state of elevator with ID=id
		'''
		# Retrieve elevator with correct id
		curElevator
		for elevator in self._elevators:
			if elevator._id = id:
				curElevator = elevator
				break;

		curElevator.update(currentFloor, goalFloors)

	def pickup(self, pickupFloor, direction):
		''' Add pickup request to pickupRequests queue.
			A pickup request is represented as a tuple 
			consisting of the pickupFloor and direction
		'''
		self._pickupRequests.add((pickupFloor, direction))