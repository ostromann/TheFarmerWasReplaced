def harvestPumpkin():
	while num_items(Items.Pumpkin_Seed) < get_world_size()**2:
		if not trade(Items.Pumpkin_Seed):
			plantCarrot()
			if can_harvest():
				harvest()
			
	
	succesful_fields = 0
	while succesful_fields <= get_world_size()**2:
		moveSomewhere()
		if get_entity_type() == Entities.Pumpkin:
			succesful_fields += 1
		else:
			harvest()
			plantPumpkin()
			succesful_fields = 0
	harvest()	
	globals[1] = 0
		
		
		
	
	
	

	