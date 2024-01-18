def plantHay():
	if get_ground_type() != Grounds.Turf:
		till()

def plantWood():
	if (get_pos_x() + get_pos_y())%2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)

def plantCarrot():
	if trade(Items.Carrot_Seed):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Carrots)

def plantPumpkin():
	if num_items(Items.Pumpkin_Seed) > 0 or trade(Items.Pumpkin_Seed):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Pumpkin)
		fieldState[get_pos_x()][get_pos_y()][6] = Entities.Pumpkin
		return True
	return False

def plantSunflower():
	if trade(Items.Sunflower_Seed):
		if get_ground_type() != Grounds.Soil:
			till()
		plant(Entities.Sunflower)

def getNextTask():

	task = None
	lowest = 1
	
	plantFunctions = [
		plantHay,
		plantWood,
		plantCarrot,
		plantPumpkin
	]
	
	for target in targets:
		quote = num_items(target[1])/target[2]
		if quote < lowest:
			lowest = quote
			task = plantFunctions[target[0]]
			
	return task