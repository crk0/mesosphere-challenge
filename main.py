class Elevator():
	def __init__(self, id, currentFloor=0):
		''' A new elevator having ID=id, current floor = 0 (ground floor)
			and no goal floors.
		'''
		self._id 			= id;
		self._currentFloor 	= currentFloor
		self._goalFloors 	= list()

	def status(self):
		''' Return triple representing state of elevator,
			state(id, current_floor, goal_floor)
		'''
		return (self._id, self._currentFloor, self._goalFloors)

	def update(self, currentFloor, goalFloors):
		''' Update the state of the elevator
		'''
		# update current floor
		self._currentFloor = currentFloor

		# remove currentFloor from goalFloor if it exists
		self._goalFloors = [floor for floor in self._goalFloors if floor[0] != currentFloor]

		# add the new goal floors
		self._goalFloors += goalFloors

	def findNextFloor(self):
		if len(self._goalFloors) == 0:
			return self._currentFloor

		if len(self._goalFloors) > 1:
			# Find optimal goal floor
			goalFloor, _ = self._goalFloors[0];
			if goalFloor > self._currentFloor:
				direction = 1
			else:
				direction = -1

			goalFloors = self._goalFloors[:]
			for gf in self._goalFloors:
				# If the goal floor request direction matches the direction
				# of the elevator, prioritise that floor.
				if gf[1] == direction:
					# If elevator is going down
					if direction < 0 and gf[0] < self._currentFloor:
						goalFloors.remove(gf)
						# find first position such that new floor is larger than goal floor
						for i in range(0, len(goalFloors)):
							if gf[0] >= goalFloors[i][0]:
								goalFloors.insert(i, gf)
								break
					# If elevator is going up
					if direction > 0 and gf[0] > self._currentFloor:
						goalFloors.remove(gf)
						# find first position such that new floor is smaller than goal floor
						for i in range(0, len(goalFloors)):
							if gf[0] <= goalFloors[i][0]:
								goalFloors.insert(i, gf)
								break

			self._goalFloors = goalFloors

		return self._goalFloors[0][0]

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
		# Update elevator with correct id
		self._elevators[id].update(currentFloor, goalFloors)

	def pickup(self, pickupFloor, direction):
		''' Add pickup request to pickupRequests queue.
			A pickup request is represented as a tuple 
			consisting of the pickupFloor and direction
		'''
		self._pickupRequests.add((pickupFloor, direction))

	def step(self):
		''' Represents one simulation tick. Process pickup requests 
			and then move all elevators as required.
		'''
		for elevator in self._elevators:
			if len(self._pickupRequests) > 0:
				request = self._pickupRequests.pop()
				self.update(elevator._id, elevator.findNextFloor(), [request])
				return
			elif len(elevator._goalFloors) == 0:
				# No requests and no goal floors, therefore nothing to do
				continue
			self.update(elevator._id, elevator.findNextFloor(), [])


if __name__ == "__main__":
	ecs = ElevatorControlSystem(1)
	print ecs.status()
	ecs.pickup(2, 1)
	ecs.pickup(4, 0)
	print ecs.status()
	ecs.step()
	print ecs.status()
	ecs.pickup(1,1)
	ecs.step()
	print ecs.status()
	ecs.step()
	print ecs.status()
	ecs.step()
	print ecs.status()
	ecs.step()
	print ecs.status()
