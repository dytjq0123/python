# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

totalLife = 90

totalDays = 365 * totalLife
totalMonths = 12 * totalLife
totalWeeks = 52 * totalLife

livedDays = 365 * age
livedMonths = 12 * age
lievedWeeks = 52 * age

resultDays = totalDays - livedDays
resultMonths = totalMonths - livedMonths
resultWeeks = totalWeeks - lievedWeeks

print(f"You have {resultDays} days, {resultWeeks} weeks, and {resultMonths} Months left.")