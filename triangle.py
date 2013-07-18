# solve the triangle problem from Yodle coding challenges

def maxTotal(matrix, size):
  # matrix is a two dimensionals array
	for i in range(size-2, -1, -1): # each row		
		
		for j in range(i+1): # each cols of the row
			currValue = matrix[i][j]
			if (currValue + matrix[i+1][j] > currValue + matrix[i+1][j+1]):
				matrix[i][j] = currValue + matrix[i+1][j]
			else:
				matrix[i][j] = currValue + matrix[i+1][j+1]		
	return matrix[0][0]

def main():
	size = 100
	matrix = [[0 for x in xrange(size)] for x in xrange(size)] 
	myInput = open('triangle.txt', 'r')
	for i in range(size):
		theLine = myInput.readline()
		arr = theLine.split()
		for j in range(i+1):
			matrix[i][j] = int(arr[j])
	print maxTotal(matrix, size)

main()
