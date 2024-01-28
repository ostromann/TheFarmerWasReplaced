def getFarmItem():
	
	batchSize = 5000
	
	targets = {
		Items.Hay : 1,
		Items.Wood : 1,
		Items.Carrot : 1,
		Items.Pumpkin : 1,
		Items.Power : 1,
		Items.Gold : 1,
		Items.Cactus : 1,
		Items.Bones : 1,
	}
	
	nextItem = None
	smallest = Infinity
	for item in targets:
		supplyRate = num_items(item)/targets[item]
		if supplyRate < smallest:
			nextItem = item
			smallest = supplyRate

	return (nextItem, batchSize)