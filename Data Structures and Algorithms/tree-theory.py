# TREE THEORY

'''
Tree bir data structure dir.

Ayni zamanda belirli ozellikleri tasiyan bir graph tir.

A is root

A is parent of B

B is a child of A

H ve I leaves olarak adlandirilan node lardir

Leaves veya leaf cocugu olmayan node lara denir


'''

# Binary Tree

"""

Node larinda en fazla 2 children node olan yapilara denir

Children sayisi max 2 olacagi icin isimleri left ve right diye adlandirilmistir

Left child right child gibi

Belirli bir leveldeki mx node sayisi 2^(l-1) l= level numarasi

Mesela 3. level de toplam maksimim node sayisi 2^ 3 = 8

height = istenilen node dan en asagida bir yapraga dogru olan path lerin toplam sayisi

root height = 3 = height of the tree

leaves right = 0 => cunku leaveslerin alt nodelari olmaz



------------------------------------------------

Full Binary Tree: Her bir node 0 ya da 2 cocuga sahip olan yapilardir

Complete Binary Tree: Ya tum level lari dolu olacak yada en azindan son level inda
node lar olabildigince sol tarafta olacak 

Perfect Binary Tree: Tum node lar 2 children a sahip olacak 
ayrica tum leaves ayni level de olacak

A Degenerate (or pathological) Tree: Her node 1 child a sahipse
Fark ettigimiz uzere linked list e cok benziyor


"""

class Node:

	# Binary Tree Nodes

	def __init__(self, key):
		self.val = key
		self.right = None
		self.left = None


# Create Root 

root = Node("A")
root.left = Node("B")
root.left.left = Node("D")
root.right = Node("C")


# Binary Search Tree


'''
Her node a solundaki kolundan ulasailabilcek butun degerlerin
node un degerinden kucuk, sag kolundan ulasilabilecek butun degerlerin o node un 
degerinden buyuk olmasinin sart ediyor

Ve tabiki binary tree olmak zorunda

BST de ordering olmasindan dolayi search hizli yapilir

En kotu durumda searching ve insertinng operation larin
time comp. O(h)'dir. h = height


'''

class Node:
	def __init__(self, key):
		self.val = key
		self.left = None
		self.right = None

# Inserting root and node

def insert(root, node):
	if root is None:
		root = node
	else:
		if root.val < node.val:
			if root.right is None:
				root.right = node
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)

r = Node(41)
insert(r, Node(65))
insert(r, Node(99))
insert(r, Node(50))
insert(r, Node(20))
insert(r, Node(11))
insert(r, Node(29))
insert(r, Node(51))

def inorder(root):
	if root:
		inorder(root.left)
		print(root.val)
		inorder(root.right)
	else:
		return None


inorder(r)














