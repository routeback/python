# Functions - Assigns a set of code or variables (known as parameters) to a single call or name

# Define - Notifies python of impending function definition

def example():
	x = 1
	y = 3
	print (x+y)
	if x < y: print(x,'is less than',y)

example()

# Most commonly to execute the whole script is the following

def main():
	example()

def addition(num1,num2):
	answer = num1+num2
	return answer

x = addition(5,6)
print(x)

# Function Parameters

# After defining our function, we can populate the variables of the parameters in multiple fashions.
# This can be accomplished through the website('TNR'... line in two ways, as a single line in the order that the defined function is passed the parameters
# Or it can be configured individually on multiple lines in order to prevent confusion and ensure that all of the parameters are mapped correctly
# Lastly, they can be directly inserted into the defined function line without having to define them when calling the function within ()
# It should be noted that the default values can be overidden when calling the function via () with different values than what is specified within the def statement


def website(font,background_color,font_size,font_color):
	print('font:',font)
	print('bg:',background_color)
	print('Font size:',font_size)
	print('Font color:',font_color)

website('TNR','White','11','Black') # Must have the exact same number of parameters and they must be in the right order

website(font='TNR',
	font_color='black',
	background_color='white',
	font_size='11',)

def website(font='TNR',
	background_color='White'):
	
	print('font:',font)
	print('bg:',background_color)

website('TNR','grey')

