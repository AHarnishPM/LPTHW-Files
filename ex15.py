#imports the argv module, reads what is put in the command
from sys import argv
#names the first word in the command script and
#the second filename.
script, filename = argv
#sets the variable txt to the output from opening the filename
#variable which is set in the second line.
txt = open(filename)
#prints the file name
print "Here's your file %r:" % filename
#prints the txt variable with the command read after it which
#converts the file to a string
print txt.read()
