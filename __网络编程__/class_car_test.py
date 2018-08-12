#class_car_test.py

'''练习类的使用'''
class Car():
	def __init__(self,make,modle,year):
		self.make = make
		self.modle = modle
		self.year = year
	def get_descriptive_name(self):
		long_name = str(self.year)+' '+self.make+' '+self.modle
		return long_name.title()
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())