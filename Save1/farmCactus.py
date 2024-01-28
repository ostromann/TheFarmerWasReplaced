def farmCactus(amount):
	
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
			
			if can_harvest() and get_entity_type() != Entities.Cactus:
				harvest()
			if get_entity_type() == None or get_entity_type() == Entities.Grass:
				if get_ground_type() != Grounds.Soil:
					till()
				if num_items(Items.Cactus_Seed) == 0:
					trade(Items.Cactus_Seed)
				plant(Entities.Cactus)
			if get_entity_type() == Entities.Cactus:
				fieldCounter += 1
			moveTo(getNextSnakePos(field, getMyPos()))
		else:
			sorted = False
			while not sorted:
				
				lastSize = None
				sorted = True
				finishedCircle = False
				moveTo((field[0][0], field[0][1]))				

				while not finishedCircle:
					
					
					if method == 1:
											
						if lastSize != None and measure() < lastSize:
							sorted = False	
							if get_pos_y() > field[0][1]:
								swap(South)
							else:
								# switch this with left upper
								while get_pos_y() < field[1][1]:
									move(North)
									swap(South)
								swap(West)
								while get_pos_y() > field[0][1]:
									move(South)
									swap(North)
						lastSize = measure()
					
					if method == 2:
						
						fieldOk = False
						while not fieldOk:
							fieldOk = True
							if get_pos_x() > field[0][0] and measure() < measure(West):
								fieldOk = False
								swap(West)
							if get_pos_x() < field[1][0] and measure() > measure(East):
								fieldOk = False
								swap(East)
							if get_pos_y() > field[0][1] and measure() < measure(South):
								fieldOk = False
								swap(South)
							if get_pos_y() < field[1][1] and measure() > measure(North):
								fieldOk = False
								swap(North)

							if not fieldOk:
								sorted = False
					


					if moveMethod == 1:
						moveTo(getNextSnakePos(field, getMyPos()))
						if get_pos_x() == field[0][0] and get_pos_y() == field[0][1]:
							finishedCircle = True
					elif moveMethod == 2:
						if get_pos_x() == field[1][0] and get_pos_y() == field[1][1]:
							finishedCircle = True
						elif get_pos_y() < field[1][1]:
							move(North)
						else:
							moveTo((get_pos_x()+1, field[0][1]))
								
						
						
				
			countBefore = num_items(Items.Cactus)
			harvest()
			fieldCounter = 0
			amount -= num_items(Items.Cactus)-countBefore
			
			
	print('cps', (startAmount-amount)/(get_time()-startTime))
