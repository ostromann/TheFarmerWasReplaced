def farmCarrot(amount):
	
	field = ((0,0), (9, 9))

	while amount > 0:
		
		if isInField(field):
		
			if can_harvest():
				countBefore = num_items(Items.Carrot)
				harvest()
				amount -= num_items(Items.Carrot)-countBefore

			if amount <= 0:
				return
				
			if get_entity_type() == None or get_entity_type() == Entities.Grass:
				if get_ground_type() != Grounds.Soil:
					till()
				if num_items(Items.Carrot_Seed) == 0:
					trade(Items.Carrot_Seed)
				plant(Entities.Carrots)
		moveTo(getNextSnakePos(field, getMyPos()))