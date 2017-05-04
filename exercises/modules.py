#!/usr/bin/python3

'''									 
Invoke the built-in help system. (This function is intended for interactive 
use.) If no argument is given, the interactive help system starts on the 
interpreter console. If the argument is a string, then the string is looked 
up as the name of a module, function, class, method, keyword, or documentation 
topic, and a help page is printed on the console. If the argument is any other 
kind of object, a help page on the object is generated.
'''									 

import sys

if len(sys.argv) < 2: # Exit if no module is specified
	sys.exit('Usage: %s module' % sys.argv[0]) # Example usage with $0 being the script name

help(sys.argv[1]) # Python help system using positional argument 1

