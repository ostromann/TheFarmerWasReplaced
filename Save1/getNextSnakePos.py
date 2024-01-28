def calcNextPos(pos, direction):
	if direction == North:
		return (pos[0], pos[1]+1)
	if direction == East:
		return (pos[0]+1, pos[1])
	if direction == South:
		return (pos[0], pos[1]-1)
	if direction == West:
		return (pos[0]-1, pos[1])
	return pos

def getNextSnakePos(field, pos):

	while pos[0] < field[0][0]:
		return calcNextPos(pos,East)
	
	while pos[0] > field[1][0]:
		return calcNextPos(pos,West)
	
	while pos[1] < field[0][1]:
		return calcNextPos(pos,North)
		
	while pos[1] > field[1][1]:
		return calcNextPos(pos,South)
		

	if field[0][1] == field[0][0] and field[0][0] == field[1][0] and field[0][1] == field[1][1]:
		return pos

	## bottom row
	if pos[1] == field[0][1] and pos[0] < field[1][0]:
		return calcNextPos(pos,East)
		
	## go home
	if (field[1][0]-field[0][0])%2 == 0: #odd
		if pos[0] < field[0][0]+2:
			if pos[0] == field[0][0] and (field[1][1]+pos[1])%2 == 1:
				return calcNextPos(pos,East)
			if pos[0] == field[0][0]+1 and (field[1][1]+pos[1])%2 == 0:
				return calcNextPos(pos,West)
			if pos[0] == field[0][0]+1 and pos[1] == field[0][1]+1:
				pos = calcNextPos(pos,West)
			return calcNextPos(pos,South)
	elif pos[0] == field[0][0]:
		return calcNextPos(pos,South)
	
	## snake
	if (field[1][0]-pos[0])%2 == 0:
		## up
		if pos[1] < field[1][1]:
			return calcNextPos(pos,North)
	elif pos[1] > field[0][1]+1:
		## down		
		return calcNextPos(pos,South)

	## end of column, move towards home
	return calcNextPos(pos,West)