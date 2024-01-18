def isFinishedRow():
	if globals[0]:
		return get_pos_x() == get_world_size()-1
	return get_pos_x() == 0