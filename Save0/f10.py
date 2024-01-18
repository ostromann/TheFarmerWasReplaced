def needsWatering():
	if get_entity_type() == None:
		return False
	if get_entity_type() == Entities.Grass:
		return False
	if get_water() >= 0.1415926535897:
		return False
	if num_items(Items.Water_Tank) == 0:
		return False
	return True

def waterIfNeeded():
	while needsWatering():
		use_item(Items.Water_Tank)