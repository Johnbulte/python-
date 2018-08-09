import re
import sys

def getAddress(port):
	pattern = r'\S+'
	f = open('1.txt')
	for line in f:
		PORT = re.match(pattern,line).group()
		if PORT == port:
			data == line 
			break
	for line in f:
		if line != '\n':
			data += line
		else:
			break
	return data

if __name__=='__main__':
	port = sys.argv[1]
	print(getAddress(port))
