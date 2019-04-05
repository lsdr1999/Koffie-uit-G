class Dienstregeling():

	def __init__(self, game):
		self.trajecten = trajecten()
		self.kritieke_stations = kritieke_stations ()
		self.max_trajecten = 7 #voor vraag 1a

def load_stations(self, filename):
	stations_data = []
	with open(filename, "r") as f:
		station_data = []
		for line in f:
			# when there is no blank newline it means there's still data.
			if not line == "\n":
				station_data.append(line.strip())
			# a blank newline signals all data of a single room is parsed.
			else:
				stations_data.append(station_data)
				station_data = []
		# append a final time, because the files do not end on a blank newline.
		stations_data.append(station_data)

def move(self, direction):
	"""
	Moves to a different station in the specified direction.
	"""
	# conditional movement.
	for directionx in self.current_room.route[direction.upper()]:
		# check if condition includes item (like: id / item).
		if directionx.isdigit() == False:
			direction_split = directionx.split("/")
			# check if item (found after splitting at "/"") is in inventory.
			if direction_split[1] in self.inventory.inventory_list:
				self.current_room = self.rooms[int(direction_split[0])]
				break
			else:
				print("Item unavailable in inventory")
		else:
			# no item needed, just go to new room.
			room_id = directionx
			self.current_room = self.rooms[int(room_id)]
