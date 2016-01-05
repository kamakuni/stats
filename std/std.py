import math

def calculate(data):
	length = len(data)
	mean = sum(data)/length
	result = math.sqrt(sum((value - mean)**2 for value in data)/length)
	return result

if __name__ == "__main__":
	data1 = [4,4,5,5,5,6,6,6,7,7]
	data2 = [1,2,3,4,5,6,7,8,9,10]

	print(calculate(data1))
	print(calculate(data2))