class Elevator():
	def __init__(self, id, currentFloor=0):
		''' A new elevator having ID=id, current floor = 0 (ground floor)
			and no goal floors.
		'''
		self._id 			= id;
		self._currentFloor 	= currentFloor
		self._goalFloor 	= list()
		self._dir 			= 0 # -1 for down, +1 for up and 0 for stationary

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
		self._goalFloor = [floor for floor in self._goalFloor if floor != currentFloor]

		# add the new goal floors
		self._goalFloor.append(goalFloors)

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
			if elevator._id == id:
				curElevator = elevator
				break;

		curElevator.update(currentFloor, goalFloors)

	def pickup(self, pickupFloor, direction):
		''' Add pickup request to pickupRequests queue.
			A pickup request is represented as a tuple 
			consisting of the pickupFloor and direction
		'''
		self._pickupRequests.add((pickupFloor, direction))

	def step(self):
		''' Represents one simulation tick. Process pickup requests 
			and then move all elevators by 1 floor as required.
		'''

		newPickupRequests = self._pickupRequests[:]
		for pickup in self.pickupRequests:
			# First check if pickup request floor exists as goal floor
			# for existing elevator
			for id, currentFloor, goalFloors in self.status():
				if pickup[0] in goalFloors:
					# Remove request since elevator already stopping there
					newPickupRequests.remove(pickup)
					break;

		self._pickupRequests = newPickupRequests

		# Update elevator states
		for id, currentFloor, goalFloors in self.status():
			if len(goalFloors) > 0:
				nextFloor = self.findNextFloor(currentFloor, goalFloors)
				newGoalFloors = [request[0] for request in self._pickupRequests]
				self.update(id, nextFloor, newGoalFloors)

	def findNextFloor(self, currentFloor, goalFloors):
		# temporary naive fcfs
		if goalFloors[0] > currentFloor:
			currentFloor += 1
		else:
			currentFloor -= 1

		return currentFloor

if __name__ == "__main__":
	pass