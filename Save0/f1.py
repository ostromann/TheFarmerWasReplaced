def scan():
	fieldState[get_pos_x()][get_pos_y()] = [
		[get_pos_x(), get_pos_y()],
		get_time(),
		get_ground_type(),
		get_entity_type(),
		get_water(),
		'ready_time',
		fieldState[get_pos_x()][get_pos_y()][6], # planted Entity
		measure(),
	]
