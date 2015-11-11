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
		# Return triple representing state of elevator,
		# state(id, current_floor, goal_floor)
		return (self._id, self._currentFloor, self._goalFloor)

	def update(self, currentFloor, goalFloors):
		# update current floor
		self._currentFloor = currentFloor

		# remove currentFloor from goalFloor if it exists
		if currentFloor in self._goalFloor:
			self._goalFloor.remove(currentFloor)

		# add the new goal floors
		self._goalFloor.union(set(goalFloors))
