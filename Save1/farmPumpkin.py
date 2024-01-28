def farmPumpkin(amount):
	
	#field = ((0,4), (4,8))
	field = ((0,0), (get_world_size()-1,get_world_size()-1))

	fieldWidht = field[1][0]-field[0][0]+1
	fieldHeight = field[1][1]-field[0][1]+1
	fieldArea = fieldWidht*fieldHeight

	pumpkinMap = emptySet()
	
	while amount > 0:
		
		if isInField(field):
											
			if can_harvest():				
				if get_entity_type() == Entities.Pumpkin:
					pumpkinMap.add(getMyPos())
					if len(pumpkinMap) >= fieldArea:
						countBefore = num_items(Items.Pumpkin)
						harvest()
						pumpkinMap = emptySet()
						amount -= num_items(Items.Pumpkin)-countBefore
						if amount <= 0:
							return
				else:
					harvest()
									
			if get_entity_type() == None or get_entity_type() == Entities.Grass:
				if get_ground_type() != Grounds.Soil:
					till()
				if num_items(Items.Pumpkin_Seed) == 0:
					trade(Items.Pumpkin_Seed)
				plant(Entities.Pumpkin)

		if len(pumpkinMap) < fieldArea:
			nextPos = getNextSnakePos(field,getMyPos())
			while (nextPos in pumpkinMap):
				nextPos = getNextSnakePos(field, nextPos)
			moveTo(nextPos)