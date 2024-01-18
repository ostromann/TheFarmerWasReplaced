def moveSomewhere():
	if isFinishedField():
		printState()
		moveTo(0,0)
		globals[0] = True
	elif isFinishedRow():
		globals[0] = not globals[0]
		move(North)
	elif globals[0]:
		move(East)
	else:
		move(West)