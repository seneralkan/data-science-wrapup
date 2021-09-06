# Bubble Sort

# Bir listede birbirine ardisik duran iki degeri sıralama yapar ve bu sureci tum liste sıralı hale gelene kadar devam eder

# https://visualgo.net/en/sorting


def BubbleSortAlgorithm(arr):
	# for every element 

	for n in range(len(arr)-1,0,1):
		# Bubble sort i schecking the every elemt in the array and sort all of them
		# The procees is always decreased due to checking and sorting the elemnts each time
		# so we need to range the len of array decrease 1 for each time 
		# until it reaches to the 0

		for k in range(n):
			# If we come to a point to switch
			if arr[k] > arr[k+1]:
				temp = arr[k]
				arr[k] =  arr[k+1]
				arr[k+1] = temp
	return arr


# Merge Sort

"""
Merge sort bir recursive algoritmadir.

Bir diziyi boyutlari 2 olacak sekilde sub arraylere bolene kadar bolmeye devam eder

Daha sonra en kucuk sub array den siralmaya baslayarak birlestirir.

"""

def MergSortAlgorithm(arr):

	"""
	Merge Sort
	"""

	if len(arr) > 1:
		mid = int(len(arr) / 2)
		leftHalf = arr[:mid]
		rightHalf = arr[mid:]


		MergSortAlgorithm(leftHalf)
		MergSortAlgorithm(rightHalf)

		i = 0
		j = 0
		k = 0

		while i < len(leftHalf) and j < len(rightHalf):
			if leftHalf[i] < rightHalf[j]:
				arr[k] = leftHalf[i]
				i += 1
			else:
				arr[k] = rightHalf[j]
				j += 1

			k += 1

		while i < len(leftHalf):
			arr[k] = leftHalf[i]
			i += 1
			k += 1

		while j < len(rightHalf):
			arr[k] = rightHalf[j]
			j += 1
			k += 1


	return arr	



"""

Insertion Sort

Sub list kullanilir

Ilk value bir sub list elemanidir ve zaten tek bir degere sahip
oldugu icin siralidir

Bu sub listenin icerisinde kalan degerler karsilastirilarak eklenir

Yani ilk sublistten sonra diger elemanlarla karsilastirip
sublist i genisletip aklinda tutuyor

Ve bunlari da digerleriyle karsilastirip sort islemini yapmaktadir

"""


def InsertionSortAlgorithm(arr):

	"""
	Insertion Sort
	"""

	for i in range(i,len(arr)):

		current_value = arr[i]
		position = i

		# Sublist

		while position > 0 and arr[position-1] > current_value:
			arr[position] = arr[position - 1]
			position -= 1

		arr[position] = current_value

	return arr



"""
Selection Sort

Sirali olmayan bir listem var

Bu listenin icerisinde en kucuk degeri bulup index 0 a atarim

Daha sonra bir sonraki en kucuk degeri bularak armamama devam ederim


"""

def SelectionSortAlgorithm(arr):

	for i in range(len(arr)-1, 0, -1):
		positionOfmax =0

		for location in range(1,i+1):
			if arr[location] > arr[positionOfmax]:
				positionOfmax = location

		print(positionOfmax)

		temp = arr[i]
		arr[i] = arr[positionOfmax]
		arr[positionOfmax] =temp

		print(arr)

	return arr


def CountSortAlgorithm(arr, maxval):

	n = len(arr)
	# index 0 dan basladigi icin maxval + 1 yapiyoruz
	m - maxval + 1
	count = [0] * m #[0,0,0,0,0.......0]
	# bos bir count listesi olusturuyoruz

	for a in arr:
		count[a] += 1
	
	i = 0

	for a in range(m):
		for c in range(count[a]):
			arr[i] = a
			i += 1

	return arr		


list = [1,1,2,3,3,4,4,4,5,6,7,7,9,8,8,8]


"""
Quick Sort


Bol ve fethet mantigini kullanir
Pivot value listeyi ikiye boler
Pivot value dan kucuk degerler listenin sol kismini buyuk degerler ise sag kismini olusturur
Recursive mantigi ile calisir


"""


def QuickSortAlgorithm(arr):
	
	quick_sort_recursion(arr,0,len(arr)-1)
		return arr


def quick_sort_recursion(arr, first, last):

	if first < last:

		splitpoint = partition(arr, first, last)

		# left right
		quick_sort_recursion(arr, first, splitpoint -1)
		quick_sort_recursion(arr, splitpoint+1, last)

		#endpoint

def partition(arr,first,last):

	# pivot value - ilk eleman secimi

	pivotValue = arr[first]

	left = first +1
	right = last

	done = False

	while not done:

		while left <= right and arr[left] <= pivotValue:
			left += 1
		
		while arr[right] >= pivotValue and right >= left:
			right -= 1

		if right < left:
			done = True

		else:
			temp  = arr[left]
			arr[left] =arr[right]
			arr[right] = temp

	temp = arr[first]
	arr[first] = arr[right]
	arr[right] = temp


	return right



"""
Heap Sort


Heap sort icin once listemixi tree ye ceviriyoruz. Yani heap insaa ediyoruz

Daha sonra insaa edilen heap i max heap e ceviriyoruz

Max heap de parent node her zaman child node dan buyuk ya da child node a esittir

Ilk ve son node un yerini degistirir ve son node u sileriz

Ve sonra ayni isleme siralama bitene kadar devam ediyoruz


"""

# Input data: 4, 10, 3, 5, 1
#          4(0)
#         /   \
#      10(1)   3(2)
#     /   \
#  5(3)    1(4)

# The numbers in bracket represent the indices in the array 
# representation of data.

# Applying heapify procedure to index 1:
#          4(0)
#         /   \
#     10(1)    3(2)
#     /   \
# 5(3)    1(4)

# Applying heapify procedure to index 0:
#         10(0)
#         /  \
#      5(1)  3(2)
#     /   \
#  4(3)    1(4)
# The heapify procedure calls itself recursively to build heap
#  in top down manner.
 


# Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap
 
def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[largest] < arr[l]:
        largest = l
 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        largest = r
 
    # Change root, if needed
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
 
        # Heapify the root.
        heapify(arr, n, largest)
 
# The main function to sort an array of given size
 
 
def heapSort(arr):
    n = len(arr)
 
    # Build a maxheap.
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapify(arr, i, 0)
 
 
# Driver code
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
n = len(arr)
print("Sorted array is")
for i in range(n):
    print("%d" % arr[i]),




# CHALLENGE 1
# Secound Great and Low

# input: 1,42,64,180
# output: 42,64

#Python uses an algorithm called Timsort:

#Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort, 
# designed to perform well on many kinds of real-world data.
# It was invented by Tim Peters in 2002 for use in the Python programming language. 
# The algorithm finds subsets of the data that are already ordered, and uses the subsets to sort the data more efficiently. This is done by merging an identified subset, called a run, with 
# existing runs until certain criteria are fulfilled. 
# Timsort has been Python's standard sorting algorithm since version 2.3. It is now also used to 
# sort arrays in Java SE 7, and on the Android platform.


def SecoundGreatLow(arr):

	unique = set(arr)

	sorted_list = sorted(unique)

	if len(sorted_list) < 2:
		return str(sorted_list[0] + " " + sorted_list[0])
 
	else:
		return str(sorted_list[0]) + " " + str(sorted_list[len(sorted_list) - 2])


# CHALLENGE 2
# Three Sum

# 10 sayisini 3 farkli sekilde 3 elemt kullanarak elde etmek
# input: 10, 2, 3, 1, 5, 3, 1, 4, -4, -3, -2
# output: "true"

import itertools

def threesum(arr):

	n = arr[0]
	del arr[0]

	l = range(len(arr))

	comb = itertools.combinations(1,3)

	for i in comb:
		#print(i)
		s=0

		for l in i:
			s += l
			print(s)

		if s == n:
			return "True"
		else:
			return "False"


threesum([10, 2, 3, 1, 5, 3, 1, 4, -4, -3, -2])







































