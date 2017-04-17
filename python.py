#!/usr/bin/python

# This tutorial is for Python 3.X
#
# Python is a Scripted Language - Operates at runtime, line by line until it reaches an error
# As opposed to compiled languages where they are compiled before being executed. 
#
# Execute with python3 python.py
# Executing without the 3 will use python2.7x
#
###

# Commenting

# Single Line Comment

'''
Multi-Line Comment
'''

'''

# Print and Strings

print('Hello World')
print("Double Quotes")
print('Concat'+'enation')
print('hello','there') # Adds a space, purpose is for combining strings and integers 
print('I am',5)

# Escape characters and using ' within a string

print('I\'m 5') # Using \ to escape a character
print("I'm 5") # Using Double quotes if you want to use single quote in the string
print('He said "Hi"') # Using single quotes if you want to use double quotes in the string

# Math

print(1+3) # Addition
print(1-3) # Subtraction
print(1*3) # Multiplication
print(1/3) # Division

print(1.5/3.6) # Float
print(4**2) # Exponents

# Variables

exVar = 100 # Integer
exVar = '100' # String
print(exVar)

exVar = 100
opVar = exVar / 5.3
print(opVar)

_100ma = 5 # Moving Average Variable that begins with a number, prefaced with an underscore 
print(_100ma)

# While Loop

condition = 1
while condition < 10: # The : is a standard to allow for tabbing on the next line, doesn't seem to work in subl. 
	print(condition)
	condition += 1
	# Alternate: condition = condition+1

while True:	# Infinite loop
	print('infinity')

# For Loops

exampleList = [1,6,7,3,6,9,0]
for x in exampleList:
	print(x)

for x in range (1,11):
	print(X)

'''
# If statements

x = 2
y = 7
z = 10

if x > y:
	print(x,'is greater than',y)
if x < y:
	print(x,'is less than',y)

if x == y: # == is a comparison operator
	print(x,'is the same as',y)

if x == 2:
	print(x,'equals the string 2')

if x <= y:
	print(x,'is less than or equal to',y)

if x >= y:
	print(x,'is greater than or equal to',y)

if z > y > x:
	print(z,'is greater than',y,'which is greater than',x)


	
