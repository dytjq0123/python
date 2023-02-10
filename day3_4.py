# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

nameTotal = name1 + name2
nameTotal = nameTotal.lower()

true1 = nameTotal.count("t")
true2 = nameTotal.count("r")
true3 = nameTotal.count("u")
true4 = nameTotal.count("e")

love1 = nameTotal.count("l")
love2 = nameTotal.count("o")
love3 = nameTotal.count("v")
love4 = nameTotal.count("e")

total1 = true1 + true2 + true3 + true4
total2 = love1 + love2 + love3 + love4

total = str(total1) + str(total2)

total = int(total)

if total <= 10 or total >= 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:    
    print(f"Your score is {total}.")
