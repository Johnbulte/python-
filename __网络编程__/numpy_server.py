import numpy
world_alcohol = numpy.genfromtxt('world_alcohol.txt',delimiter=',',dtype=str)
print(type(world_alcohol))
print(world_alcohol)
print(help(numpy.genfromtxt))