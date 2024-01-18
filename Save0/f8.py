def plantSomething():

	nextPlantTask = None

	if get_entity_type() == None or get_entity_type() == Entities.Grass:
		nextPlantTask = getNextTask()
		
	if nextPlantTask != None:
		nextPlantTask()