def farmHay(amount):
	
	field = ((0,0),(3,3))

	while amount > 0:
		
		if isInField(field):

			if can_harvest():
				countBefore = num_items(Items.Hay)
				harvest()
				amount -= num_items(Items.Hay)-countBefore
	
			if get_entity_type() == None and get_ground_type() != Grounds.Turf:
				till()
				
			if amount <= 0:
				return
		
		moveTo(getNextSnakePos(field, getMyPos()))