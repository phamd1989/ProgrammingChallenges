# How does the algorithm work?
# Calculate the rank of the word 'GOOGLE'

# First, order all characters in the word alphabetically 
# and build a dictionary to keep track of all characters
# -> orderedArray = [E, G, G, L, O, O]
# -> frequencyDict = {(G, 2), (O: 2), (L: 1), (E: 1)}

# Second, build the positionNumber array by reading each
# character of the original word from left to right, 
# for each character, find its position in the orderedArray
# and calculate how many characters traveled to get there
# save this number in the positionNumber array and 
# delete that letter in the orderedArray.
# -> positionNumberArray: [1, 3, 3, 1, 1, 0]

# Third, calculate the frequencyRepetition also by reading each
# character of the original word from left to right, 
# for each character, calculate the factorial of the value for each 
# (key, value) pair in the dictionary and multiply them together
# then decrease the value in the pair(key, value) whose key match the
# current character that we are reading in.
# For 'G', the frequencyRepetition is 2! * 2!, then 
# frequencyDict = {(G, 2), (O: 2), (L: 1), (E: 1)} 
# -> frequencyDict = {(G, 1), (O: 2), (L: 1), (E: 1)} 

# Finally, calculate rank for each character by multiply its position 
# the positionNumberArray with the factorial of (len(word) - curr_pos - 1)
# and divides by the frequencyRepetition
# For example, 'G' -> (5!) * (1) / (2!*2!*1!*1!)
#   		 'O' -> (4!) * (3) / (1!*2!*1!*1!) 	
# 			 '0' -> (3!) * (3) / (1!*1!*1!*1!)
# 			 ....
# Sum all these values and add 1. That's the rank!


import math, sys, timeit

# calculate the frequency repetition of all characters in the dictionary
def frequencyRepetition(dictionary):
	value = 1
	for item in dictionary.items():
		value = value * math.factorial(item[1])
	return value

# build a dictionary to keep track of all characters and its frequency
def frequencyDict(charArray):
	dictionary = {}
	for ch in charArray:
		if ch not in dictionary:
			dictionary[ch] = 1
		else:
			dictionary[ch] = dictionary[ch] + 1
	return dictionary

# create a positionNumber array for multiplication purpose
def positionNumber(charArray, charArraySorted):
	array = []
	for ch in charArray:
		count = 0 # count how many chars to its left
		while(charArraySorted[count] != ch):
			count = count + 1
		# remove a char from the sorted array
		charArraySorted.remove(charArraySorted[count])
		array.append(count)
	return array

def calculateRank(word):
	# initialization
	charArray = list(word)
	charArraySorted = list(word)
	charArraySorted.sort()	
	dictionary = frequencyDict(charArray)
	positionNumberArray = positionNumber(charArray, charArraySorted)
	
	rank = 0 # rank of the word
	size = len(charArray)
	for i in range(size):
		if (positionNumberArray[i] != 0):
			# See above for more information about this formula
			rank = rank + positionNumberArray[i] * math.factorial(size - i -1) / frequencyRepetition(dictionary)
		# decrease the frequency of the character in the dictionary
		dictionary[charArray[i]] = dictionary[charArray[i]] - 1

	return rank + 1

def test():    
	# get the word from the command line
    word = sys.argv[1]
    # calculate the word's rank
    print calculateRank(word)		

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test", number = 1))
