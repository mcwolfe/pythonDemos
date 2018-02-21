def move(fr, to,number):
	if number == 1:
		brick = tower[fr].pop()
		tower[to].append(brick)
	else:
		tempTow = abs(fr+to-3)	
		move(fr, tempTow,number-1)
		brick = tower[fr].pop()
		tower[to].append(brick)
		move(tempTow,to,number-1)
		


tower = []
for i in range(0,3):
	tower.append([])
	
for i in range(1,6):
	tower[0].insert(0,i)
	
	
	
print(tower)
move(0,1,5)
			