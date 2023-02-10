#city = input("What's name of the city you grew up in?\n")
#pet = input("What's your pet's name?\n")
#print("your band name could be " + city + " " + pet)



print("Welcom to the tip calculator.")
bill = input("What was the total bill? $")
bill = float(bill)
people = input("How many people to split the bill? ")
people = int(people)
percentage = input("What percentage tip would you like to give? 10, 12, or 15? ")
percentage = int(percentage)

pay = bill / people
pay = float(pay)
tip = pay * percentage / 100
tip = float(tip)
total = pay + tip
total = round(total, 2)
#total = float(total)
print("Each person should pay: $" + str(total))
print("Each person should pay: $", total)
print(f"Each person should pay: ${total}")