name = "Ibrahim"
print(name);


#lower case

print(name.lower())

#upper case
print(name.upper())

#boolean case

print(name.isupper()) #it will show false because the name is not a upper case value

name = "IBRAHIM" #upper case value
print(name.isupper())

name = "ibrahim" #lower case value
print(name.islower())

#coverter plus boolean

print(name.upper().isupper()) #it will change to upper case first, then it will check if the value is upper case or not. Lastly, it will show a true and false value

print(name.lower().islower())


#length of the string

#use 'len' to show the length

print(len(name)) 


#finding the index of a string
#use '[]'
#the index will always start with 0 not 1 

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])


#index function
#finding where a specific letter or something is located inside the parameter

print(name.index("b"))


#replace statement

name = "Ibrahim"

print(name.replace("Ibrahim", "Rayed"))