def farmGold():

	directions = [North, East, South, West]
	d = 0
				
	while get_entity_type() != Entities.Hedge:

		if get_entity_type() == None or get_entity_type() == Entities.Grass:
			plant(Entities.Bush)		
		
		if can_harvest():
			if get_entity_type() == Entities.Bush:		
				if num_items(Items.Fertilizer) == 0:
					trade(Items.Fertilizer)
				use_item(Items.Fertilizer)
			else:
				harvest()
			
	while True:
		if get_entity_type() == Entities.Treasure:
			harvest()
			return
		d = (d+1)%4 # try move right
		if not move(directions[d]):
			d = (d+3)%4 # try move straigt
			if not move(directions[d]):		
				d = (d+2)%4 # try move left