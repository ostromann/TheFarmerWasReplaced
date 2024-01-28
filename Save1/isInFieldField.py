def isInField(field):

	if get_pos_x() >= field[0][0] and get_pos_x() <= field[1][0]:
		if get_pos_y() >= field[0][1] and get_pos_y() <= field[1][1]:
			return True

	return False