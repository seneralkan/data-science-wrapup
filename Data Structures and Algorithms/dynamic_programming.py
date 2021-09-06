"""
Dynamic Programming

Buyuk bir problemi kuck problemlere bolerek cozmek ve bu kucuk
problemlerin sonuclarini depolayarak ayni sonuclarin tekrar
hesaplanmasini onler. PS: Recursion da depolama islemi yok

Her bir kucuk problem birleserek buyuk problem icin cozum yolu olusturur

Dynamic programming en guzel ornegi fibonacci sayilaridir


"""

# Fibonacci numbers with recursion

def recur_fib(n):
	"""
	Recursion function for fibonacci sequence
	"""

	# base case

	if n <= 1:
		return n
	else:
		return (recur_fib(n-1) + recur_fib(n-2))


"""

Fibonacci sayilarinda goruldugu uzere pek cok repeated operation calisir
Divide big problem to the small problem and one solution will contribute to other solution

Time Complexity: T(n) = T(n-1) + T(n-2) which is exponential
Bu method cok fazla repeated work yapiyor bu nedenle fibonacci number n icin uygun bir yontem degildir

Simdi dynamic prog kullanalim
Yani daha onceden hesaplanmis fibonacci numberlari depolayalim

"""

def dynamic_fib(n):

	fibo_list = [0,1]

	while len(fibo_list) < n+1:
		fibo_list.append(0)

	if n <= 1:
		return n
	else:
		if fibo_list[n-1] == 0:
			fibo_list[n-1] = dynamic_fib(n-1)
		if fibo_list[n-2] == 0:
			fibo_list[n-2] = dynamic_fib(n-2)

		fibo_list[n] = fibo_list[n-2] + fibo_list[n-1]

	return fibo_list[n]

dynamic_fib(0)
dynamic_fib(10)

"""
Time Complexivity of Dynamic Programming  is O(n)

which is faster than recursion
"""


"""
Challange - Catalan Numbers
------------------
Dynamic Programming i ne zaman kullaniriz ?
	- Eger cozumumuz sub problemlere bolununebiliyorsa

Memoization nedir ?
------------------
	- Bir degeri her seferinde hesaplamaktansa, bir kere hesaplayip bir yere depolayip
daha sonra baska yerde kullanilmaya verilen addir.
"""

# Recursive Method

def recur_catalan(n):

	# base case

	if n <= 1:
		return 1

	res = 0

	for i in range(n):
		res  += recur_catalan(i) * recur_catalan(n- i -1)
	
	return res

# Dynammic Programming

def dynamic_catalan(n):

	# base case
	if n <= 1:
		return 1

	# storing catalan numbers
	catalan = [0 for i in range(n+1)]

	# initiliazing first 2 values
	catalan[0], catalan[1] =  1,1

	# fill the list
	for i in range(2, n+1):
		catalan[i] = 0
		for j in range(i):
			catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]

	return catalan[n]












