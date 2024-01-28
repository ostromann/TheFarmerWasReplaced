def farmWood(amount):
	
	field = ((0,0), (9,9))
	
	while amount > 0:
		
		if isInField(field):
		
			if can_harvest():
				countBefore = num_items(Items.Wood)
				harvest()
				amount -= num_items(Items.Wood)-countBefore
				

			
			if get_entity_type() == None or get_entity_type() == Entities.Grass:
					if (get_pos_x()+get_pos_y())%2 == 0:
						plant(Entities.Tree)	
					else:
						plant(Entities.Bush)
			if amount <= 0:
				return
							
		moveTo(getNextSnakePos(field, getMyPos()))