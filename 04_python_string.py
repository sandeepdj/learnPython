# In Python everything is object and string are an object too. 
# Python string can be created simply by enclosing characters in the double quote.

#For example:
var = "Hello World!"

# Accessing Values in Strings
# Python does not support a character type, these are treated as strings of length one, 
# also considered as substring.
# We use square brackets for slicing along with the index or indices to obtain a substring.
var1 = "Sandeep!"
var2 = "Software Testing"
print ("var1[0]:",var1[0])
print ("var2[1:5]:",var2[1:5])

# Various String Operators
################################################################################################################
# [ ]     :: Slice- it gives the letter from the given index 
x="Sandeep"
print x[1] # output - s

################################################################################################################
# [ : ]   ::  Range slice-it gives the characters from the given 
x2="Sandeep" 
print x2[1:3]  # O/P- an
print x2[0:3]  # O/P- San

################################################################################################################

# in      :: 	Membership-returns true if a letter exist in the given string
x3="Sandeep" 
print "d" in x3  # O/P - True
print "x" in x3  # O/P - False

################################################################################################################

# not in    :: Membership-returns true if a letter exist is not in the given string
x4="Sandeep" 
print "x" not in x4 # O/P - True
print "S" not in x4 # O/P - Flase

################################################################################################################
# r/R       :: Raw string suppresses actual meaning of escape characters.
            # Print r'\n' prints \n and print R'/n' prints \n
print r'\n'

################################################################################################################
# % - Used for string format 
    #    :: %r - It insert the canonical string representation of 
    #           the object (i.e., repr(o)) %s- It insert the presentation string representation 
    #    of the object (i.e., str(o)) %d- it will format a number for display
name = 'Sandeep'
number = 99
print'%s %d' % (name,number)	
################################################################################################################
# +       :: It concatenates 2 strings
x5="Sandeep" 
y="99" 
print x5+y

################################################################################################################
# *      :: Repeat	It prints the character twice.

x6="Snadeep" 
y6="99" 
print x6*2