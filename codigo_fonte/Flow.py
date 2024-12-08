import queue
from collections import defaultdict

class Graph:
	CONST_INF = int(1e9)

	def __init__(self, numberOfVertex):
		self.size = numberOfVertex
		self.graph = []
		self.graph[0:self.size] = [[] for _ in range(self.size)]
		self.capacity = []
		self.capacity[0:self.size] = [[0]] * self.size

	def addEdge(self, vertexFrom, vertexTo, cost):
		self.graph[vertexFrom].append([vertexTo, cost])

	def ShortestPathFasterAlgorithm(self, source, distance, path):
		n = self.size

		distance[0:n] = [self.CONST_INF] * n
		path[0:n] = [-1] * n
		cnt = []
		cnt[0:n] = [0] * n
		inqueue = []
		inqueue[0:n] = [False] * n
		vertexQueue = queue.Queue()

		distance[source] = 0
		vertexQueue.put(source)
		inqueue[source] = True

		while(not vertexQueue.empty()):
			current = vertexQueue.get()
			inqueue[current] = False

			for vertex, cost in self.graph[current]: 
				if(self.capacityMatrix[current][vertex] > 0 and
					 distance[current] + cost < distance[vertex]):
					distance[vertex] = distance[current] + cost
					path[vertex] = current
					if(not inqueue[vertex]):
						vertexQueue.put(vertex)
						inqueue[vertex] = True
						cnt[vertex] += 1
						if(cnt[vertex] > n):
							return False
		return True

	def minCostFlow(self, source, destiny, edges):
		costMatrix = [[0 for x in range(self.size)] for y in range(self.size)]
		self.capacityMatrix = [[0 for x in range(self.size)] for y in range(self.size)]

		for vertexFrom, vertexTo, cost, capacity in edges:
			self.addEdge(vertexFrom, vertexTo, cost)
			self.addEdge(vertexTo, vertexFrom, -cost)
			costMatrix[vertexFrom][vertexTo] = cost
			costMatrix[vertexTo][vertexFrom] = -cost
			self.capacityMatrix[vertexFrom][vertexTo] = capacity
			self.capacityMatrix[vertexTo][vertexFrom] = 0

		flow = 0
		cost = 0
		distance = []
		path = []
		while(flow < self.CONST_INF):
			self.ShortestPathFasterAlgorithm(source, distance, path)
			if(distance[destiny] == self.CONST_INF):
				break

			currentFlow = self.CONST_INF - flow
			currentVertex = destiny
			while(currentVertex != source):
				currentFlow = min(currentFlow,
					 self.capacityMatrix[path[currentVertex]][currentVertex])
				currentVertex = path[currentVertex]

			flow += currentFlow
			cost += currentFlow * distance[destiny]
			currentVertex = destiny
			while(currentVertex != source):
				self.capacityMatrix[path[currentVertex]][currentVertex] -= currentFlow
				self.capacityMatrix[currentVertex][path[currentVertex]] += currentFlow
				currentVertex = path[currentVertex]
		return flow

	# Retorna pra onde o fluxo vai quando sai do vertice fromVertex
	# Ignora o vertice 0, predefinido como source
	# Retorna -1 se não passa fluxo por esse vertice
	def flowPathFromVertex(self, fromVertex):
		for toVertex, cost in self.graph[fromVertex]:
			if(toVertex != 0 and self.capacityMatrix[int(fromVertex)][int(toVertex)] == 0):
				return toVertex
		return -1

# graph = Graph(13)
# edges = []
# edges.append([1, 2, 0 ,1])
# edges.append([1, 3, 0, 1])
# edges.append([1, 4, 0, 1])
# edges.append([1, 5, 0, 1])
# edges.append([2, 6, 10, 1])
# edges.append([2, 7, 11, 1])
# edges.append([2, 8, 11, 1])
# edges.append([2, 9, 12, 1])
# edges.append([3, 6, 10, 2])
# edges.append([3, 7, 9, 1])
# edges.append([3, 8, 12, 1])
# edges.append([4, 7, 9, 1])
# edges.append([4, 8, 10, 1])
# edges.append([4, 9, 10, 1])
# edges.append([5, 8, 9, 1])
# edges.append([5, 9, 10, 1])
# edges.append([5, 10, 10, 1])
# edges.append([6, 11, 0, 1])
# edges.append([7, 11, 0, 1])
# edges.append([8, 11, 0, 1])
# edges.append([9, 11, 0, 1])
# edges.append([10, 11, 0, 1])
# print(graph.minCostFlow(1, 11, edges))
