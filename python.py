#!/usr/bin/python3

# This tutorial is for Python 3.X
#
# Python is a Scripted Language which operates at runtime, line by line until it reaches an error or completes its operations
# This is as opposed to compiled languages where they are compiled into a binary application.
#
# Commands should be executed with the python3 command
# Executing without the trailing 3 will use python 2.x
#
###

# Commenting

# Single Line Comment

'''
Multi-Line Comment
'''

# Print and Strings

print('Hello World') # Single Qoutes
print("Double Quotes")
print('Concat'+'enation') # Merging two strings
print('hello','there') # Adds a space, purpose is for combining strings and integers on the same line

# Escape characters and using ' within a string

print('I am',5) # Print both the string and integer with a space inbetween
print('I\'m 5') # Using \ to escape a character and allow for the ' to be printed to std out
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
while condition < 10: # The : is a standard to allow for tabbing on the next line
	print(condition)
	condition += 1
	# Alternate: condition = condition+1

# Infinite loop

while True:
	print('infinity')

# For Loops

exampleList = [1,6,7,3,6,9,0]
for x in exampleList:
	print(x)

for x in range (1,11):
	print(X)

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

