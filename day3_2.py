# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

first = year % 4
second = year % 100
third = year % 400

if first == 0:
    if second != 0:
        print("Leap year.")
    else:
        if third == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
else:
    print("Not leap year.")