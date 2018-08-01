#A Python variable is a reserved memory location to store values. 
#In other words, a variable in a python program gives data to the computer for processing.
#Data_Types - Numbers, List, Tuple, Strings, Dictionary


# Declare variable
a = 100
print(a)   # print a -in python 2

# Redeclare varibale

a = 200
print(a)   # print a -in python 2


#Concatenate Variables
b = 300

#print("sandeep" + a) # o/p - TypeError: cannot concatenate 'str' and 'int' objects

print(a+b) # This will concatenate



###### LOCAL AND GLOBAL VARIABLE #################

def shoeLocal():
    a = "I'm local variable" 
    print(a)
shoeLocal()
print(a)

# # variable declared using global e.g( global a ) it will override previous value


def shoeLocal():
    global a 
    print(a)
a = "Now i'm global here"
shoeLocal()
print(a)



#Delete a variable

x = 'i will be deleted'
print(x)

del x
print(x)   # NameError: name 'x' is not defined