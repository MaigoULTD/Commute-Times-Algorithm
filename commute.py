import datetime
print ("*****PUT TIME IN HH:MM:SS FORMAT*****")
print("If non-applicable, leave empty")

walk = raw_input("Walking Time:")
car = raw_input("Car Time:")
wait= raw_input("Waiting time:")
bus = raw_input("Bus time:")
train = raw_input("Train time:")


if walk != '':
	walk = walk.split(',')
	walk = map(lambda x: x.split(':'), walk)
	sumWalk = 0
	for List in walk:
		h, m, s = [int(i) for i in List]
		walkT = 3600*h + 60*m + s
		sumWalk += walkT
if walk == '':
	sumWalk = 0


if car != '':
	car = car.split(',')
	car = map(lambda x: x.split(':'), car)
	sumCar = 0
	for List in car:
		h, m, s = [int(i) for i in List]
		carT = 3600*h + 60*m + s
		sumCar += carT
if car == '':
	sumCar = 0

if wait != '':
	wait = wait.split(',')
	wait = map(lambda x: x.split(':'), wait)
	sumWait = 0
	for List in wait:
		h, m, s = [int(i) for i in List]
		waitT = 3600*h + 60*m + s
		sumWait += waitT
		 
if wait == '':
	sumWait = 0

if train != '':
	train = train.split(',')
	train = map(lambda x: x.split(':'), train)
	sumTrain = 0
	for List in train:
		h, m, s = [int(i) for i in List]
		trainT = 3600*h + 60*m + s
		sumTrain += trainT
if train == '':
	sumTrain = 0

if bus != '':
	bus = bus.split(',')
	bus = map(lambda x: x.split(':'), bus)
	sumBus = 0
	for List in bus:
		h, m, s = [int(i) for i in List]
		busT = 3600*h + 60*m + s
		sumBus += busT
if bus == '':
	sumBus = 0


	

totalTime = (sumWalk + sumCar + sumWait + sumTrain + sumBus)
print("\n")
print("Walk time is, " + str( sumWalk))
print("Car time is, "  + str( sumCar))

print("Wait time is, " + str( sumWait))


print("Train time is, " + str( sumTrain))


print("Bus time is, " + str( sumBus))

print("Total time is " + str(totalTime))





