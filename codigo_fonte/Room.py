# Define uma classe para Sala, que sera utilizado pelo algoritmo.
# Tem como membro os mesmos parametros usado pelo Room.txt fornecido pelo Sids
# e recebe os mesmos no construtor
class Room:
	def __init__(self, uniqueId, bld, cap, roomType, special, name):
		self.uniqueId = uniqueId
		self.bld = bld
		self.cap = int(cap)
		self.roomType = roomType
		self.special = special
		self.name = name
		self.dayHour = [[0 for _ in range(18)] for _ in range(8)]

	def assignClass(self, day, hour, requestID):
		self.dayHour[day][hour] = requestID

	def isRoomFullDayHour(self, day, hour):
		return False if self.dayHour[day][hour] == 0 else True 
