# 0: goEast
# 1: mode (0: default, 1: plantPumpkin)
globals = [True, 0]
targets = [
	[0, Items.Hay, 1500],
	[1, Items.Wood, 1000],
	[2, Items.Carrot, 2000],	
	[3, Items.Pumpkin, 3000]
]

fieldState = []
for i in range(get_world_size()):
	row = []
	for j in range(get_world_size()):
		row.append(['','','','','','',''])
	fieldState.append(row)




moveTo(0,0)

while True:
	quick_print(globals[1])
	scan()
	moveSomewhere()
		
	if globals[1] == 0:
		harvestStuff()		
		plantSomething()
		
	elif globals[1] == 1:
		harvestPumpkin()
		
	waterIfNeeded()
	switchMode()
			
			
