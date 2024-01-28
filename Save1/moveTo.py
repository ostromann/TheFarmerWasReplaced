def moveTo(pos):
	while get_pos_x() < pos[0]:
		move(East)
	while get_pos_x() > pos[0]:
		move(West)
	while get_pos_y() < pos[1]:
		move(North)
	while get_pos_y() > pos[1]:
		move(South)