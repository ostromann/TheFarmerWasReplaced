needed = None

#determine needs
hayFactor = 1	
woodFactor = 1
carrotFactor = 2
pumpkinFactor = 2

divisor = hayFactor + woodFactor + carrotFactor

pumpkinCounter = 0
	
while True:

	sumOfItems = num_items(Items.Hay)+num_items(Items.Wood)+num_items(Items.Carrot)
	unitSize = sumOfItems/divisor
	
	supplyRateHay = num_items(Items.Hay)/unitSize/hayFactor
	supplyRateWood = num_items(Items.Wood)/unitSize/woodFactor
	supplyRateCarrot = num_items(Items.Carrot)/unitSize/carrotFactor
	supplyRatePumpkin = num_items(Items.Pumpkin)/unitSize/pumpkinFactor
	
	newNeeded = Items.Hay
	smallest = supplyRateHay
	
	if supplyRateWood < smallest:
		newNeeded = Items.Wood
		smallest = supplyRateWood
		
	if supplyRateCarrot < smallest:
		newNeeded = Items.Carrot
		smallest = supplyRateCarrot
	

	if supplyRatePumpkin < smallest:
		newNeeded = Items.Pumpkin
		smallest = supplyRatePumpkin

	
	if newNeeded != needed:
		if newNeeded == Items.Pumpkin:
			pumpkinCounter = 0
		needed = newNeeded
		quick_print(supplyRateHay, supplyRateWood, supplyRateCarrot, needed)
	

	if needed == Items.Hay:
		if get_entity_type() == None or can_harvest() and harvest():
			if get_ground_type() != Grounds.Turf:
				till()
	

	if needed == Items.Carrot:
		if get_entity_type() == None or can_harvest() and harvest():
			if get_entity_type() != Entities.Carrots:
				if get_ground_type() != Grounds.Soil:
					till()
				if num_items(Items.Carrot_Seed) == 0:
					trade(Items.Carrot_Seed)
				plant(Entities.Carrots)
		

	if needed == Items.Wood:
		if get_entity_type() == None or can_harvest() and harvest():
			if (get_pos_x()+get_pos_y())%2 == 0:
				if get_entity_type() != Entities.Tree:
					plant(Entities.Tree)	
			else:
				if get_entity_type() != Entities.Bush:
					plant(Entities.Bush)	


	if needed == Items.Pumpkin:		

		# slightly more complex harvesting
		if can_harvest():	
			if get_entity_type() == Entities.Pumpkin:
				pumpkinCounter += 1
				if pumpkinCounter == get_world_size()**2:
					harvest()
			else:
				harvest()

		if get_entity_type() == None:
			if get_ground_type() != Grounds.Soil:
				till()
			if num_items(Items.Pumpkin_Seed) == 0:
				trade(Items.Pumpkin_Seed)
			plant(Entities.Pumpkin)
			pumpkinCounter = 0
			
	move(East)
	if get_pos_x() == 0:
		move(North)
		