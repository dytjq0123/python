programming_dictionary = {
    "Bug":"An error in a program that prevents the program from running as expected.",
    "Function":"A piece of code that you can easily call over and over again.",
    
}

print()

#Retrieving items from dictionary.
# print(programming_dictionary["Bug"])

#Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

#Create an empty dictionary.
empty_dictionary = {}

#Wipe an exising dictionary.
# programming_dictionary ={}
# print(programming_dictionary)

#Edit an item in a dictionary.
programming_dictionary["Test"] = "test"
print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])