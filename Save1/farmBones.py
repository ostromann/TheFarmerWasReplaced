def farmBones(amount):
	
	field = ((0,0), (get_world_size()-1, get_world_size()-1))

	fieldWidht = field[1][0]-field[0][0]+1
	fieldHeight = field[1][1]-field[0][1]+1
	fieldArea = fieldWidht*fieldHeight

	fieldCounter = 0


	startAmount = amount
	startTime = get_time()	
	method = 2
	moveMethod = 1

	while amount > 0:

		if fieldCounter < fieldArea:
			
			if not isInField(field):
				moveTo(getNextSnakePos(field, getMyPos()))
			
			if can_harvest() and get_entity_type() != Entities.Dinosaur:
				harvest()
			if get_entity_type() == None or get_entity_type() == Entities.Grass:
				if num_items(Items.Egg) == 0:
					trade(Items.Egg)
				use_item(Items.Egg)
			if get_entity_type() == Entities.Dinosaur:
				fieldCounter += 1
			moveTo(getNextSnakePos(field, getMyPos()))
		else:
			cycleSwaps = Infinity
			while cycleSwaps > 10:
				cycleSwaps = 0
				finishedSortCircle = False
				moveTo((field[0][0], field[0][1]))				
				while not finishedSortCircle:
					swapCounter = Infinity
					while swapCounter > 0:
						swapCounter = 0
						
						measureValue = measure()
						measureSwapField = measure(West)
						if measureValue != None and measureSwapField != None and get_pos_x() > field[0][0] and measureValue < measureSwapField:
							swapCounter += 1
							swap(West)
						
						measureValue = measure()
						measureSwapField = measure(East)
						if measureValue != None and measureSwapField != None and get_pos_x() < field[1][0] and measureValue > measureSwapField:
							swapCounter += 1
							swap(East)
						
						measureValue = measure()
						measureSwapField = measure(South)
						if measureValue != None and measureSwapField != None and get_pos_y() > field[0][1] and measureValue < measureSwapField:
							swapCounter += 1
							swap(South)
						
						measureValue = measure()
						measureSwapField = measure(North)
						if measureValue != None and measureSwapField != None and get_pos_y() < field[1][1] and measureValue > measureSwapField:
							swapCounter += 1
							swap(North)
							
						cycleSwaps += swapCounter
				
					moveTo(getNextSnakePos(field, getMyPos()))
					if get_pos_x() == field[0][0] and get_pos_y() == field[0][1]:
						finishedSortCircle = True
				quick_print('swaps', cycleSwaps)
			
			quick_print('start harvesting')

			moveTo((field[0][0], field[0][1]))
			finishedHarvestCircle = False
			while not finishedHarvestCircle:			
				countBefore = num_items(Items.Bones)
				harvest()
				amount -= num_items(Items.Bones)-countBefore
				moveTo(getNextSnakePos(field, getMyPos()))
				if get_pos_x() == field[0][0] and get_pos_y() == field[0][1]:
					finishedHarvestCircle = True
			fieldCounter = 0