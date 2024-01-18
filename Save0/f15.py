# Can this really go to trash?
def foo():
	while (get_pos_x(), get_pos_y()) != starting_pos:
		if get_entity_type() != Entities.Pumpkin:
			while get_entity_type() != None and not harvest():
				pass
			fieldState[get_pos_x()][get_pos_y()][6] = ''
			all_pumpkins = False
			
			moveTo(starting_pos[0], starting_pos[1])
			globals[0] = starting_direction
			globals[1] = 1 # plantPumpkinMode
		else:
			moveSomewhere()
	
	if all_pumpkins:
		harvest()
		for i in range(get_world_size()):
			for j in range(get_world_size()):
				fieldState[i][j][6] = ''