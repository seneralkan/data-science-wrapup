"""
GRAPH THEORY


Graph lar tree lerden daha genel data structure lardir

Trees ozel graph cesididir

Gercek hayatta karsilasilan problemleri graph theory kullanarak ifade edebiliriz

Mesela bir ulkedeki hava trafigi yada internet baglantisi

Graphs iki bilesenden olusur

- Node (vertex) 

- Edge = connection between two nodes

- Edge iki yonlu olabilir

	- Eger edge tek yonlu ise directed graph ya da dia=graph denir

	- Eger yonu yok ise un-directed graph denir

- Path ise edge le ile birbirine baglanan node sirasi

- Cycle graph: bir path in bir node dan baslayip ayni node da bitmeso


"""

"""

Adjacency Matrix ve List

Graph i ifade etmenin (bilgisayara tanimlamanin) en kolay yollarindan biri 2 boyutlu matrix kullanmaktir

Her bir row ve column graph in node laridir

djacent komus demektir. Tanimi ise 2 tane node un bir edge ile baglanmasi sonucu ortaya cikan yapiya adjacent denir

Kucuk graph lar icin adjacency  matrix kullanmak gorme acisindan kolaylik saglar

Am gordugumuz gibi matrix icerisinde cok fazla sayida bos cell var. Yani bosuna yer kapliyorlar.
Bu bosluklari azaltmanin yolu graph da edge sayisini artirmak. Bu nedenle eger bir graph da edge sayisi fazla ise adjacency matrix kullanmak avantajlidir

Eger cok graph da cok sayida edge yoksa adjacency matrix yerine adjacency list kullanmayi tercih etmeliyiz

Adjacency list matrix e gore dah fazla space efficient
"""


# Adjacency List with Python

# Graph() bos graph yaratir
# addVertex(): graph icerisine ndeo ekler
# addEdge(fromVert, toVert): iki node u birbirine baglayan direted edge ekler
# addEdgge(fromVert, toVert, weight): iki node u birbirine baglayana weighted ve directed edge ekler
# getVertex(vertKey): graph icerisindeki node u bulur
# gerVertices(): node lari return eder


class Vertex:
	def __init__(self, key):
		#  node constructor
		self.id = key
		self.connectedTo = {}

	def addNeighbor(self, neighbor, weight=0):
		self.connectedTo[neighbor] = weight

	def __str__(self):
		return str(self.id) + "connected To:" + str([x.id for x in self.connectedTo])


	def getConnections(self):
		return self.connectedTo.keys()


	def getId(self):
		return self.id

	def getWeight(self, neighbor):
		return self.connectedTo[neighbor]


class Graph:

	def __init__(self):
		self.vertList = {}
		self.numVertices = 0


	def addVertex(self, key):

		self.numVertices += 1
		newVertex = Vertex(key)
		self.vertList[key] = newVertex
		return newVertex

	def getVertex(self, n):
		if n in self.vertList:
			return vertList[n]
		else:
			return None

	# icinde mi degil mi true veya false seklinde donduruyor
	def __contains__(self, n):
		return n in self.vertList

	def addEdge(self,f, t, cost =0):
		if f not in self.vertList: # f:from, t: to
			nv = self.addVertex(f)
		if t not in self.vertList:
			nv = self.addVertex(t)

		self.vertList[f].addNeighbor(self.vertList[t], cost)

	def getVertices(self):
		return self.vertList.keys()

	def __iter__(self):
		return iter(self,vertList,values())


g = Graph()

g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addVertex(5)
g.addVertex(6)
g.vertList


g.addEdge(1,2, 0)
g.addEdge(1,3, 0)
g.addEdge(3,5, 0)

for v in g:
	print(v)
	print(v.getConnections())



"""
Depth First Search (DFS)

Derin oncelikli arama olarak gecer
Bir tree(graph) traverse algoritmasidir
Depth First Search ilk once alt seviyesinde bulunan node larin aranasi durumudur
Once sol tarafi traverse edip sonra sag tarafa gecip islemlerini yapiyor

"""

# set ile tanimlamamizn sebibi unique yapilari bulma kolayca ekleme ve cikarma islemi yapma
graph = {"A": set(["B", "C"]),
		 "B": set(["A", "D", "E"]), 
		 "C": set(["A", "F"]),
		 "D": set(["B"]),
		 "B": set(["B", "F"]),
		 "F": set(["C", "E"]),
}


print(graph)


def dfs(graph, start):
	visited = set()
	stack = [start]
	while stack:
		vertex = stack.pop()
		if vertex not in visited:
			visited.add(vertex)
			stack.extend(graph[vertex] - visited)
		print(visited)
		return visited


df(graph, "A")


"""
Breadth First Search (DFS)

Sig oncelikli arama olarak gecer
Bir tree (graph) traverse algoritmasidir
Breadth First Search ilk once ayni seviyede bulunan node larin aranmasi durumudur
"""


graph = {"A": set(["B", "C"]),
		 "B": set(["A", "D", "E"]), 
		 "C": set(["A", "F"]),
		 "D": set(["B"]),
		 "B": set(["B", "F"]),
		 "F": set(["C", "E"]),
}


print(graph)



def bfs(graph, start):

	visited = set()
	queue = [start]
	
	while queue:
		vertex = queue.pop(0)
		if vertex not in visited:
			visited.add(vertex)
			queue.extend(graph[vertex] - visited)
	print(visited)		
	return visited

bfs(graph, "A")


"""
Challenge - Vertex Covering

a= ["(A,B,C,D)", "(A-B, A-D, B-D, A-C)", "(A,B)"]
Output: yes
b= ["(A,B,C,D)", "(A-B, A-D, B-D, A-C)", "(C)"]
Output: (A-B,A-D,B-D)
c= ["(A,B,C,D)", "(A-B, A-D, B-D, A-C)", "(C,B)"]
Output: (A-D)
"""


def VertexCovering(a):
	vertices = a[2][1:-1].split(",")
	graph = a[1][1:-1].split(",")
	failed = []

	if len(vertices[0]) == 0:
		return a[1]
	for i in graph:
		flag  = True
		for x in vertices:
			if x in i:
				flag=False
		if flag:
			failed.append(i)
	if len(failed) > 0:
		return "(" + ",".join(failed) + ")"
	return "yes"

a= ["(A,B,C,D)", "(A-B, A-D, B-D, A-C)", "(A,B)"]
b= ["(A,B,C,D)", "(A-B, A-D, B-D, A-C)", "(C)"]
c= ["(A,B,C,D)", "(A-B, A-D, B-D, A-C)", "(C,B)"]

VertexCovering(a=a)



















