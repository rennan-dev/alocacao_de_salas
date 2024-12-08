from Room import Room

lessonsFileName = "Output/Lessons.txt"
outputLessonsFileName = "Output/UnalocatedLessons.txt"
buildingsFileName = "SIDS/Buildings.txt"
hoursFileName = "SIDS/Hours.txt"
reservationsFileName = "SIDS/Reservations.txt"
roomsFileName = "SIDS/Rooms.txt"
outputCsv = "Output/Rooms.csv"

diasDaSemana = "Domingo,Segunda,Terca,Quarta,Quinta,Sexta,Sabado\n"
hours = []
hourCount = 17
roomObjects = []

def readRooms():
	file = open(roomsFileName)
	file.readline()
	rooms = {}
	for currentLine in file:
		data = currentLine.split()
		if len(data) != 6:
			data.append("Sem nome") 
		room = [data[5], data[1]]
		rooms[data[0]] = room
		roomObject = Room(data[0], data[1], data[2], data[3], data[4], data[5])
		roomObjects.append(roomObject)
	return rooms

def readLessons(buildings):
	file = open(lessonsFileName)
	outputFile = open(outputLessonsFileName, "w")
	file.readline()
	lessons = {}
	unalocatedLessons = []
	dias = diasDaSemana.split(",")
	tipo = {"1": "Sala", "2": "Lab", "3": "Ateliê"}
	for currentLine in file:
		data = currentLine.split()
		itemList = [data[5], data[6], data[9], data[1]]
		lessons[data[0]] = itemList
		if(int(data[9]) == -1):
			unalocatedLessons.append([data[0], data[7], int(data[5])-1, int(data[6])-1, data[8]])
		else:
			for room in roomObjects:
				if(int(room.uniqueId) == int(data[9])):
					room.assignClass(int(data[5]), int(data[6]), int(data[0]))

	motivos = ["Sem Sala", "Outro motivo"]
	for lesson in unalocatedLessons:
		empty = 0
		for room in roomObjects:
			if(int(room.bld) == lesson[1] and int(room.roomType) == lesson[4]
				and room.isRoomFullDayHour(lesson[2], lesson[3]) == False):
				empty = 1
		outputFile.write("Pedido número: " + lesson[0] + 
		" Prédio: " + buildings[lesson[1]] + " Dia: " + 
		dias[lesson[2]] + " Horas: " + hours[lesson[3]] + 
		" Tipo: " + tipo[lesson[4]] + " Motivo: " +
		motivos[empty] + "\n")
	return lessons

def readBuildings():
	file = open(buildingsFileName)
	file.readline()
	buildings = {}
	for currentLine in file:
		data = currentLine.split()
		buildings[data[0]] = data[2]
	return buildings

def readHours():
	file = open(hoursFileName)
	file.readline()
	for currentLine in file:
		data = currentLine.split()
		line = [data[1], "-", data[2]]
		hour = " ".join(line)
		hours.append(hour)

def readReservations():
	file = open(reservationsFileName)
	file.readline()
	reservations = {}
	for currentLine in file:
		data = currentLine.split()
		while(len(data) < 8):
			data.insert(6, "-1")
		name = " ".join(data[7:])
		reservations[data[1]] = name
	return reservations	

def outputToCsv(rooms, lessons, buildings, reservations):
	file = open(outputCsv, "w")
	for room in rooms:
		data = rooms[room]
		header = ["Sala:", data[0], ",", "Prédio:", buildings[data[1]], ",", diasDaSemana]
		file.write(" ".join(header))
		currentHour = 1
		for hour in hours:
			line = [hour]
			line.append(",")
			for currentDay in range(1, 7):
				line.append(",")
				for lesson in lessons:
					lessonData = lessons[lesson]
					# print(lessonData)
					if(int(lessonData[0]) == int(currentDay) and int(lessonData[1]) == int(currentHour) and
						int(lessonData[2]) == int(room)):
						line.append(reservations[lessonData[3]])
						break
			line.append("\n")
			file.write(" ".join(line))
			currentHour = currentHour + 1


rooms = readRooms()
buildings = readBuildings()
readHours()
lessons = readLessons(buildings)
reservations = readReservations()
outputToCsv(rooms, lessons, buildings, reservations)
