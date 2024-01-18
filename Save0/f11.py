def printState():
	quick_print('field state:')
	for row in fieldState:
		quick_print('+---+---+---+---+')
		rowString = '|'
		for col in row:
			rowString = rowString + '0.3'
			rowString = rowString + '|'
		quick_print(rowString)
	quick_print('+---+---+---+---+')
			