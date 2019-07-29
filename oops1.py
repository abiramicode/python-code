Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # oops
>>> 
>>> 
>>> class sample:
	def getdata(self,x,y,z):
		self.x=x
		self.y=y
		self.z=z
	def display(self):
		print(self.x+self.y+self.z)

		
>>> 
>>> s1=sample()
>>> s2=sample()
>>> 
>>> s1.getdata(2,4,6)
>>> s1.display()
12
>>> 
>>> s2.getdata(3,6,9)
>>> s2.display()
18
>>> 
>>> s1.y
4
>>> 
>>> s2.y
6
>>> 
>>> 
