	
class Animal(object):
	def __init__(self, sound, name, age):
		self.sound=sound
		self.name=name
		self.age=age
	def eat(self, food):
		print(self.name + " is eating " +food)
	def sleep(self, dream):
		print("the " + self.age + " year old " + self.name + " is dreaming of " + self.sound)
	


class Bird(Animal):
	def __init__(self, sound, name, age):
		super().__init__(sound, name, age)
	def fly(self):
		print("the bird " + self.name +  " is flying")
	def eatchicken(self, name):
            print("Barbara is eating " + name) 
	
	
class Chicken(Animal):
	def _init__(self, sound, name , age):
		super().__init__(sound, name, age)
	def fly(self):
		print("oops the chicken " +self.name +" cant fly")
	def eatchicken(self):
            print("I am Bob, Barbara ate me, i cant fly :(")

		
