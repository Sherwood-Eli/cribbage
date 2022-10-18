def findFifteen(i, val, stack):
	global cards
	global score
	x = i + 1
	go = True
	found = False
	while go and x < 13:
		num = x + 1
		if found:
			found = False
		if num > 10:
			num = 10
		for y in range(0, cards[x]):
			if (val > (num)):
				stack.append(num)
				found = findFifteen(x, val - (num), stack)
				if found == False:
					stack.remove(num)
			elif (val == (num)):
				found = True
				for z in stack:
					print(z, end= " ")
				if x > 9:
					if x == 10:
						print("j +2")
					elif x == 11:
						print("q +2")
					else:
						print("k +2")
				else:
					print(num, "+2")
				score+=2
			else:
				go = False
				found = False
		x+=1
	return found


cards = []
score = 0
for x in range(0,13):
	cards.append(0)
	
x = 1
while x < 6:
	i = input("card " + str(x) + ": " )
	if (i.isalpha()):
		i = i.lower()
		if i == "k":
			cards[12]+=1
		elif i == "q":
			cards[11]+=1
		elif i == "j":
			cards[10]+=1
		elif i == "a":
			cards[0]+=1
		else:
			print("Not Accepted")
			x -= 1
	else:
		i = int(i) 	
		if (i < 2) or (i > 10):
			print("Not Accepted")
			x -= 1
		else:
			cards[i-1] += 1
	x += 1
	
print("Your points:")
	
for x in range(0, len(cards)):
	for y in range(0, cards[x]):
		findFifteen(x, 15 - (x + 1), [x+1])

for x in range(0, len(cards)):
	total = 1
	z = cards[x]
	if z > 1:
		for y in range(0, 2):
			total = total * z
			z -= 1
		print(cards[x], " ", (x+1), "'s +", total, sep="")
		score+=total
print("Total: ", score)
