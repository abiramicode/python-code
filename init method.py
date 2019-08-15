Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class sample:
	def __init__(self,name,age,city):
		self.name=name
		self.age=age
		self.city=city
	def show(self):
		return self.name,self.age,self.city


	
>>> s=sample("Abirami",21,"salem")
>>> s
<__main__.sample object at 0x032CD4F0>
>>> s.show()
('Abirami', 21, 'salem')
>>> s.city
'salem'
>>> s.age
21
>>> s.name
'Abirami'
>>> 
