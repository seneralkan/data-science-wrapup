# Args & kwargs

'''
--------- ARGS --------
Degisken sayili parametre vermenin bir yolu
List/tuple objelerini unpacak yapar ama dictionary objelerini yapmaz
'''

def sum(number):
	res = 0
	for e in number:
		res += e
	return res
	
number = [1,2,3,4]

sum(number)



# args nin anlami en basta tuple gibi bir objem vardi ama bunu tek  tek
# elemanlara ayirdim demek

def sum(*args):
	res = 0
	for e in args:
		res += e
	return res
	
# args = 1,2,3,4 oldugunu varsayacak, yani args in tek tek
# elemanlarina ayrilmis hali 1,2,3,4 o zaman orginali:
# args = (1,2,3,4)


def sum(*number):
	res = 0
	print(type(number))
	print(number)
	for e in number:
		res += 0

	return res

sum(1,2,3,4)

sum(1,2)

sum(1,2,3,4,5,6,7,8)


# Liste olarak toplam islemi icin ise asagidaki gibi bir islem gerceklestirebiliriz.

def sum_2(*args):
	res = 0
	print(type(args))
	print(args)
	for e in args:
		for j in e:
			res +=j
	return res


sum_2([1,2])

'''
--------- KWARGS -------

Fonksiyona degisken sayida keyword argument verebilmemizi saglar

'''


def students(**kwargs):

	for v in kwargs.values():
		print(v)


students(name = "Jake", student_number: "4317468913")


def students(**kwargs):
	print(students)
	for v in students:
		print(v)

students(name = "Jake", student_number: "4317468913")


"""
USING ARGS and KWARGS TOGETHER

Kullanim sirasi onemli oluyor bu sekildeki kullanimlarda

once args sonra kwwargs


"""


def weird(*args, **kwargs):
	res = 0
	for e in args:
		res += 0

	for k, v in kwargs.items():
		print(k. ":", v)

	return res


weird(1,3,4, name ="Sener", student_number="4197648934")


"""

UNPACKING

"""

L = [1,2,3,4]

print(L)

print(*L) # tek tek elemalarini unpack yapiyor
# Output: 1 2 3 4

L2 = [20.21]

merged_l = [*L, *L2]

# unpack edip elemanlari tek tek yazdirmis oluyoruz
merged_l # output : 1 2 3 4 20 21

# unpack islemi dictionary icin:

d1 = {"name": "Sener", "number": 421}
d2 = {"lastname": "John", "grade": 77}

d_merged = (**d1, **d2)

d_merged



d1 = {"name": "Sener", "number": 421}
d3 = {"name": "Melis", "number": 321}
d4 = {"name": "Ahmet", "number": 414}


d_merged_3 = (**d1,  **d3, **d4)

d_merged_3

# output olarak en guncel olan degeri bize verecek
# unique ise direk deger olarak aliyor zaten

# yani: "name": "Ahmet", "number": 414

st_list = [*"hey"]


# Output icin stringin her harfini unpack yapiyor
# h,e,y seklinde
st_list

#------------------------------------------------------------

"""
CLOUSURE

Outer fonksiyonu cagirdiktan sonra bile inner funcion in outer func 

scope una erisebilmesine denir

"""


def outer();
	msg = "Hey"

	def inner():
		print(msg)

	return inner()

outer()

# output: Hey

# bu ornek daha once yaptiklarimizdan farkli degi. inner function enclosing scope a erisip msg degiskenini bastirabildi

def outer();
	msg = "Hey"

	def inner():
		print(msg)

	return inner #obje olarak return ediyoruz

f = outer()

f

# Output: <function___main__.outer.<locals>.inner()>
# yani obje olarak dondu
# Function call yapmadigim surece obje olarak kalacak
# Bunu asagidaki gibi yazdigimizda clouser mantigi calismis olacak

f()

# ve output: Hey

# Burada outer function cagirilmis olsa da onu scope unda tanimlanan degiskenlere hala erisebildik


def outer();
	msg = msh

	def inner():
		print(msg)

	return inner

hi_f = ("hi")

hey_f = ("hello")

hi_f() # output hi

hey_f() # output hello


"""

DECORATOR

Decoratorlar baska fonksiyonlari parametre olarak kabul edip
yeni bir fonksiyonalite ile yerni bir fonksiyon donduren yapilardir.

"""


def print_func():
	print("hey")


def decorator_func(func):
	def wrapper_func():
		return func()

	return wrapper_func


decorator_print = decorator_func(print_func)

decorator_print()


# Var olan fonksiyona fonksiyonuy degistirmeden yeni bir davranis kazandiracagiz

def decorator_func():
	def wrapper_func():
		print(f"the name of the function is {func.__name__}")
		return func()

	return wrapper_func

decorator_print = decorator_func(print_func)

decorator_print()

# ---------- !!!!!!!!!! ------------

# Ayni seyi su sekilde de yapabilirdik
# sununla ayni print_func = decorator_func(print_func)

@decorator_func
def print_func():
	print('hey')


# func un yaptigi aslinda fonksiyonumuzu func a input olarak vermek

print_func()

def func(name, number):
	print(f"Name: {name}, number:  {number}")


func("sener", 234)


def decorator_func(func):
	def wrapper_func(*args):
		print(f"the name of the function is {func.__name__}")
		return func(*args)

	return wrapper_func


@decorator_func  # func = decorator_func(func)
def func(name. number):
	print(f"Name: {name} number: {number}")


func("Jack", 213)

# ---------- Onemli !!!!! -------------
# decorator mantiginda wrapper func calisacagindan icerisine arguman almasi gerektigini belirtmemiz gerekiyor

# --------------------------------------------------------------------------------------------

"""

CLASS TANIMLAMAK

Fonksiyonlarda belirli fonksiyonalite ifade eden kodlari bir araya getirmeyi gormustuk.
Class mantiginda hem fonksiyonalite hem de bir veiyi bir arada tutma yoluna bakacagiz

Class icerisindeki verilere attribute fonksiyonlara method diyecegiz

Diyelim ki  bir is yeri calisanlari kodumuzda ifade etmek istiyoruz. Sanki bu class mantigi ile uyumlu
Her calisanin farkli farkli ozellikleri ve yaptiklari isler (methodlar) var.

Class icerisinde method yazilirken classtan yaratilan objeyi methodlar ilk arguman olarak alirlar
Istedigimiz adi verebiliriz ama genellikle self diye gecer

"""

# class objeler olusturmak icin bir kaliptir sadece


# self ile referans vermis oluyoruz obje inputlarina 		
class Employee:
	"""docstring for Employee"""
	def __init__(self, name, last, age, pay):
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay

emp_1 = Employee("Hugh", "Jackmon", "62", 500000)

# Yukarida yarattigimiz bir obje oldu. Employee class inin bir objesi

emp_2 = Employee("Charlie", "Brown", "42", 300000)
		
emp_1.mame # output: Hugh

# Method

class Employee:
	"""docstring for Employee"""
	def __init__(self, name, last, age, pay):
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay
	# self otamatik olarak diger attributlari aliyor
	def fullname(self):
		print(f"{self.name} {self.last}")


emp_1 = Employee("Hugh", "Jackmon", "62", 500000)

# Yukarida yarattigimiz bir obje oldu. Employee class inin bir objesi

emp_2 = Employee("Charlie", "Brown", "42", 300000)


emp_1.fullname()

# Class Variable


"""

Instance Variable: Classtan yaratilan objelerin kendine ozgu degiskenleri
Yukaridaki ornekte name, last, age, pay gibi

Class Variable: Class tan yaratilan tum objelerde paylasilan degiskenlerdir

Instance variable her obje icin farkli olabilir ama class variable hepsi icin ayni olmak zorunda

Tum calisanlar arasinda hangi verinin paylasilmasinin isteyebilirim ? Mesela sirket herkese
ayni yuzdelik zam uyguluyorsa bunun yuzdesinin class variable olarak tutabilirim



"""

class Employee:
	#class variable
	raise_percent = 1.05

	"""docstring for Employee"""
	def __init__(self, name, last, age, pay):
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay

	def apply_raise(self):
		self.pay = self.pay * .raise_percent
	
emp_1.apply_raise()

# Hata verecek 


# Class variable larina ulasabilmek icin ya genel Class uzerinden ya da
# o sirada olusturdugumuz obje uzerinden ulasmamiz lazim 

emp_1.raise_percent

Employee.raise_percent
# Both output: 1.05


# Obje uzerinden ulasabilmemiz ve hata vermemesi icin 
# Employee.raise_percent olarak belirtmem gerekiyor
# veya self.raise_percent olarak belirtmem gerekiyor
class Employee:
	#class variable
	raise_percent = 1.05

	"""docstring for Employee"""
	def __init__(self, name, last, age, pay):
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay

	def apply_raise(self):
		self.pay = self.pay * Employee.raise_percent
	
emp_1.apply_raise()

print(emp_1.__dict__) # objenin attributelarini donduruyor

# Class variable i instance (classtan olusturulan bir obje) uzerinden
# guncellemek sadece o objenin o degerini gunceller

emp_1.raise_percent = 1.07

print(emp_1.__dict__) 
print(emp_2.__dict__)

# Kac tane calisan oldugunu class variable olarak tutmak
# degisen bir variable eklemek istiyorum
# her yewnio calisam geldiginde toplam calisani 1 artirmka istiyorum



class Employee:
	#class variable
	raise_percent = 1.05
	num_emp = 0

	"""docstring for Employee"""
	def __init__(self, name, last, age, pay):
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay
		Employee.num_emp += 1 

	def apply_raise(self):
		self.pay = self.pay * Employee.raise_percent


emp_1 = Employee("Hugh", "Jackmon", "62", 500000)
emp_2 = Employee("Charlie", "Brown", "42", 300000)



"""
Class ve Static Method

"""

# Class Method

# @classmethod decorator methodu ilk arguman olarak instance almak yerine class i alacak sekilde gunceller

class Employee:
	#class variable
	raise_percent = 1.05
	num_emp = 0

	"""docstring for Employee"""
	def __init__(self, name, last, age, pay):
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay
		Employee.num_emp += 1 

	def apply_raise(self):
		self.pay = self.pay * Employee.raise_percent

	@classmethod
	# bu sekilde self atamiyoruuz onun yerine class i atiyoruz
	def set_raise(cls, amount):
		cls.raise_percent = amount



emp_1 = Employee("Hugh", "Jackmon", "62", 500000)
emp_2 = Employee("Charlie", "Brown", "42", 300000)


Employee.set_raise(1.6)

#instance lar uzerinden de islem gerceklesebiliyor
emp_1.set_raise(2.3)



# Alternative Constructor

# Diyelim ki bize class i olustururken input olarak string veriyorlar
# ve bizim bundan name, age, gibi bilgileri kendimiz cikarmamiz lazim


emp_1_str = "James-Hunter-32-5000"
emp_1_str = "Charlie-Brown-22-3000"

# Split ederek her bir degeri instance variable a atamis oluyoruz
name, last, age, pay = emp_1_str.split("-")

emp_1 = Employee(name, last, age, pay)


# Ama belki herzaman bu sekilde vermeyecegiz
# String olarak input geldiginde objenin bu sekilde olusmasi icin baska nasil 
# bir mekanizma kullanabiliriz ?

class Employee():
	class variable
	raise_percent = 1.05
	num_emp = 0
	"""docstring for Employee"""
	def __init__(self, name, last, age, pay):
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay

	def apply_raise(self):
		self.pay = self.pay * Employee.raise_percent

	@classmethod
	# bu sekilde self atamiyoruuz onun yerine class i atiyoruz
	def set_raise(cls, amount):
		cls.raise_percent = amount

	@classmethod
	def from_string(cls, emp_str):
		name, last, age, pay = emp_1_str.split("-")
		# yeni calisan yaratip dondurecek
		return cls(name, last. int(age), float(pay))

emp_1_str = "James-Hunter-32-5000"
emp_1_str = "Charlie-Brown-22-3000"

emp_1 = Employee.from_string(emp_1_str)

emp_1.pay

#----------------------

# Static Method

# regular methodlar (ilk gorduklerimiz) classs in instance(olusturulan objeyi)
# methodlara otomatik olarak arguman olarak veriyor
# Static methodlar otomatik olarak bir sey vermeyen methodlar olacak

# Instance veya class a methodun icerisinde erisim olmuyorsa static olarak tanimlamak daha iyi olabilir.


class Employee():
	class variable
	raise_percent = 1.05
	num_emp = 0
	"""docstring for Employee"""
	def __init__(self, name, last, age, pay):
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay

	def apply_raise(self):
		self.pay = self.pay * Employee.raise_percent

	@classmethod
	# bu sekilde self atamiyoruuz onun yerine class i atiyoruz
	def set_raise(cls, amount):
		cls.raise_percent = amount

	@classmethod
	def from_string(cls, emp_str):
		name, last, age, pay = emp_1_str.split("-")
		# yeni calisan yaratip dondurecek
		return cls(name, last. int(age), float(pay))

	@staticmethod
	def holiday_print(day);
		if day == "weekend"
			print("this is an day off")
		else:
			print("This is not an day off")

Employee.holiday_print("weekend")
# Output: this is an day off

emp_1 = Employee("James", "Hunter", "32", 5000)
emp_1.holiday_print("workday")
#  Output: This is not an day off


# ------------------------------

"""
INHERITANCE

Inheritance belirttigimiz baska classlardaki method ve attributelara erismmemizi saglar

Diyelim ki farkli tipte calisanlar yaratmak istiyorum. IT, Data Science, HR, Operation


"""


class Employee():
	class variable
	raise_percent = 1.05
	num_emp = 0
	"""docstring for Employee"""
	def __init__(self, name, last, age, pay):
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay

	def apply_raise(self):
		self.pay = self.pay * Employee.raise_percent


# Hangi class tan inherit etmke istedigimnizi parantezin icersine yaziyoruz

# Inherit ettigimiz class a parent/super class, inherit edene de child/subclass denir


emp_1 = Employee("Hugh", "Jackmon", "62", 500000)
emp_2 = Employee("Charlie", "Brown", "42", 300000)


class IT(Employee):
	pass

# It nin icersine hicbir sey yazmasak da Employee nin ozelliklerine erisimi var

# IT nin icerisinde bulamazsa aradigini, inherit ettigi yere gidip bakacak

# IT nin icersinde __init__ methodu yok

# O yuzden gidip Employee class ina bakacak

it_1 = Employee("Sener", "Alkan", "26", 10000)  

it_1.name
# Output: Sener

it_1.__dict__

help(IT)

# o zaman super class daki methodlarina da ulasabiliyor

it_1.apply_raise()
it_1.pay

# Diyelim ki IT dekilerin yuzdelijk maass degisimini farkli bir deger olarak belirlemek istiyorum


class IT(Employee):
	raise_percent =1.2


it_1 = Employee("Sener", "Alkan", "26", 10000)


it_1.pay

it_1.raise_percent
# Bunun orani farkli 

it_1.apply_raise()

it_1.pay
# Output 120000
# ve yeni degere gore guncelleme yapti

## Yani subclass da yapilan degisikler super class i ETKILEMIYOR

# Diyelim ki IT cilere yeni bir ozellik olarak hangi programlama dilini de bildiklerini de eklemek istiyorum

class IT(Employee):
	raise_percent =1.2
	def __init__(self, name, last, age, pay, lng):
		# burada init oldugundan super class init i yerine buranin initine oncelik veriyor
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay
		self.lng = lng

# Ama bunun yerine kolayca asagidaki gibi yapabiliriz

class IT(Employee):
	"""docstring for IT"""
	def __init__(self, name, last, age, pay):
		super().__init__(name, last, age, pay)
		self.lng = lng


# Boylce ayni kodu tekrar yazmamis olduk
# Zaten superclass in init methodu yapiyoprsa yeniden yazmayta gerek yok

       
it_1 = Employee("Sener", "Alkan", "26", 10000, "python")

it_1.lng

class HR(Employee):

	raise_percent = 1.3
	"""docstring for HR"""
	def __init__(self, name, last, age, pay, experience):
		super().__init__(name, last, age, pay)
		self.experience = experience

	def print_exp(self):
		print(f"This employee has {self.experience} years of experience")


ik_1 = IK("Charlie", "Brown", "56", 6000, 30)

ik_1.print_exp()

isinstance(ik_1, HR) #true

isinstance(ik_1, Employee) #true

isinstance(IK, Employee) # true

isinstance(IT, Employee) # true

isinstance(HR, IT) # false
		
#--------------------------------------


# Magic Method

# Magic Method u kullanarak bazi built-in davaranislari degistirebiliriz

# Magic Methodlar ___ ile cevrilidir.

# Bunlara dunder method da denir


class Employee():

	raise_percent = 1.05
	num_emp = 0

	def __init__(self, name, last, age, pay);
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay
		Employee.num_emp += 1

	def apply_raise(self):
		self.pay = self.pay * raise_percent



emp_1 = Employee("Hugh", "Jackmon", "62", 500000)
emp_2 = Employee("Charlie", "Brown", "42", 300000)


# __str__()

# Objenin okunabilir bir tanimini olustururuz


class Employee():

	raise_percent = 1.05
	num_emp = 0

	def __init__(self, name, last, age, pay);
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay
		Employee.num_emp += 1

	def apply_raise(self):
		self.pay = self.pay * raise_percent

	def __str__(self):
		return f"Employee(name={self.name}, last={self.name}, age={self.age}, pay={self.pay})"




emp_1 = Employee("Hugh", "Jackmon", "62", 500000)
print(emp_1)

# Output: Employee(name=Hugh, last=Jackmon age=62, pay=500000)



# __add__()

class Employee():

	raise_percent = 1.05
	num_emp = 0

	def __init__(self, name, last, age, pay);
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay
		Employee.num_emp += 1

	def apply_raise(self):
		self.pay = self.pay * raise_percent

	def __str__(self):
		return f"Employee(name={self.name}, last={self.name}, age={self.age}, pay={self.pay})"

	def __add__(self, other):
		return self.pay + other.pay


emp_1 = Employee("Hugh", "Jackmon", "62", 500000)
emp_2 = Employee("Charlie", "Brown", "42", 300000)

emp_1 + emp_2
# Output will be the sum of the employees pay(salary)


# __len__



class Employee():

	raise_percent = 1.05
	num_emp = 0

	def __init__(self, name, last, age, pay);
		self.name = name
		self.last = last
		self.age = age
		self.pay = pay
		Employee.num_emp += 1

	def apply_raise(self):
		self.pay = self.pay * raise_percent

	def __str__(self):
		return f"Employee(name={self.name}, last={self.name}, age={self.age}, pay={self.pay})"

	def __add__(self, other):
		return self.pay + other.pay

	def __len__(self):
		return len(self.name)

len(emp_1)

# Output olarak emp1 in name karakter uzunlugunu vererk class imiza fonksiyonalite kazandirmis oluyoruz

#-------------------------------------------------------------------


"""
GENERATOR

Diyelim ki elimdeki listenin elemanlarinin karesini almak istiyorum


"""

# Fonksiyonlar returdan sonra fonskiyon islemlerini kapatiyorlar

def square(l):
	res = []

	for e in l:
		res.append(e*e)

	return res


l = [1,2,3]

square(l)

# Output: 1, 4, 9
# res icerise append olarak hepsini hesaplayip 
# hesaplamalari bittikten sonra return islemini yapiyor



# Generatorlarda bu durum farkli olarak yiled ile yeni gelecek olan degerleri beslewmis oluyoruz

# Peki bu degerleri bir anda istemesem de, ben sordukca bana dondurse

# Bunu generator mantigi ile yapacagiz


def square_generator(l):

	for e in l:
		yield e*e

l = [1,2,3]
g = square_generator(l)

g
# Output: <generator object >

# Generatorlar butun cevabi hafizada tutmazlar biz sordukca degerleri dondururler
# Generatorlar iterator dur. next ile sonraki degere ulsabiliriz
# fakat elinde deger kalmazsa iterasyonlardaki gibi exaust olup donguyu bitiriyorlar

next(g)
# Output: 1
next(g)
# Output: 4
next(g)
# Output: 9

next(g)

# exhaust oldu. Bir daha bastan baslatmak istiyorsam bir daha yaratmam lazim

# Ayrica degerler arasindaki iterasyonu for ile dondurup yazdirabilirim

g = square_generator(l)


# Degerler arasinda iterasyonu for dongusu ile de yapabilirim

for res in g:
	print(res)


# List comprehension Olusturur gibi Generator Olusturma

l = [x*x for x in [1,2,3,4,5]]


l # Output: 1,4,9,16

g = (x*x for x in [1,2,3,4,5])

g
# artik bir generator oldu
# Ve Output: <generator object>

next(g)

# It sorted from 2, because we wrote next(g) before
# and since it remembers the state that it is started 


for e in g:
	print(e)

# Generator i Listeye Donusturme

g = (x*x for x in [1,2,3,4,5])

next(g)

list(g)

# Output: [1,4,9,16,25]

l = [1,2,3,4,5]
g = square_generator(l)


list(g)
# Output: [1,4,9,16,25]


next(g)
# Error veriyor cunku exaust oldu


# Neden Generrators

'''

Kisa yoldan iterator yaratmamiza olanak sagliyor

Ugrastiklarimiz az elelmanlar olunca cok farkini anlamayabiliriz ama fazla sayida
elemanlarla ugrasiyorsak, hepsini bir anda hafizada tutmaya calismak 
cok yer kaplayabiliyor

Generator istenildiginde elemanlari dondurdukleri icin bu hafiza sorununna iyi gelebiliyor


'''

# Generator Exercise

def range_generrator(start, end, step):
	current= start

	while current < end:
		yield current
		print(current)
		current += stop


r = range_generrator(1,20,3)

next(r)





















