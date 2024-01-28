def farmPower(amount, keepFactor):
	

	field = ((0,0),(get_world_size()-1, get_world_size()-1))
	#field = ((0,0), (2,2))

	fieldWidht = field[1][0]-field[0][0]+1
	fieldHeight = field[1][1]-field[0][1]+1
	fieldArea = fieldWidht*fieldHeight

	petalMap = {}
	harvestMode = False

	startAmount = amount
	startTime = get_time()	
	while amount > 0:	
		if isInField(field):
				
			if can_harvest():	
				if get_entity_type() != Entities.Sunflower:
					harvest()				
				elif harvestMode == True:
						countBefore = num_items(Items.Power)
						harvest()
						petalMap.pop(getMyPos())
						amount -= num_items(Items.Power)-countBefore
						if amount <= 0:
							return

			if harvestMode == False:
				
				if get_entity_type() == None or get_entity_type() == Entities.Grass:
					if get_ground_type() != Grounds.Soil:
						till()
					if num_items(Items.Sunflower_Seed) == 0:
						trade(Items.Sunflower_Seed)
					plant(Entities.Sunflower)
				
			if get_entity_type() == Entities.Sunflower:
				petalMap[getMyPos()] = measure()

		if len(petalMap) == fieldArea:
			harvestMode = True
		if len(petalMap) <= fieldArea*keepFactor:
			harvestMode = False
		
		maxPetals = 0
		for pos in petalMap:
			maxPetals = max(maxPetals, petalMap[pos])
			
		nextPos = getMyPos()
		validPosition = False
		while (validPosition == False):
			nextPos = getNextSnakePos(field, nextPos)
			if(harvestMode == True):
				validPosition = nextPos in petalMap and petalMap[nextPos] == maxPetals
			else:
				validPosition = nextPos not in petalMap
		moveTo(nextPos)