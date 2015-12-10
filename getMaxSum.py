#!/usr/bin/python
import sys

def readFile(txtFile):
    with open(txtFile, 'rb') as inputTriangle:
    	triangle = []
    	for row in inputTriangle:
    		triangle.append(row.replace("\n",'').rstrip().split(" "))
    		maxLength = len(row.replace("\n",'').rstrip().split(" "))
    return triangle

def fetchMax(triangle):
	for i in range(len(triangle)):
		#flip the tree (bottom up)
		flippedIndex = int((len(triangle)-1)-i)
		for j, element in enumerate(triangle[flippedIndex-1]):
			element = int(element)
			#try to get the max of the left and right child and sum it with the top element
			try:
				triangle[flippedIndex-1][j] = int(triangle[flippedIndex-1][j]) + max(int(triangle[flippedIndex][j]), int(triangle[flippedIndex][j+1]))
			#if you cant get the right child, grab the left and it's left (neighbors)
			except IndexError:
				triangle[flippedIndex-1][j] = int(triangle[flippedIndex-1][j]) + max(int(triangle[flippedIndex][j]), int(triangle[flippedIndex][j-1]))

		#base case, when the whole triangle is reduced
		if (len(triangle[flippedIndex-1])==1):
			return triangle[flippedIndex-1][j];

print fetchMax(readFile(sys.argv[1]))
