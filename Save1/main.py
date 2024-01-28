farmItem = None
		
while True:
	
	farmItem = getFarmItem()
	
	if farmItem[0] == Items.Hay:
		farmHay(farmItem[1])
		
	if farmItem[0] == Items.Wood:
		farmWood(farmItem[1])
		
	if farmItem[0] == Items.Carrot:
		farmCarrot(farmItem[1])

	if farmItem[0] == Items.Pumpkin:		
		farmPumpkin(farmItem[1])

	if farmItem[0] == Items.Power:
		farmPower(farmItem[1], 0.1)
			
	if farmItem[0] == Items.Gold:		
		farmGold()
		
	if farmItem[0] == Items.Cactus:		
		farmCactus(1)
		
	if farmItem[0] == Items.Bones:		
		farmBones(1)