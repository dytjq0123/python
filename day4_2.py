# Split string method
#names_string = input("Give me everybody's names, separated by a comma. ")
import random


names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇



#random_Number = random.randint(0, len(names)-1)

#selected_Name = names[random_Number]

selected_Name = random.choice(names)

print(selected_Name + " is going to buy the meal today!")