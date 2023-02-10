print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")
        
    wants_photh = input("Do tou want a photo taken? Y or N. ")
    if wants_photh == "Y":
        bill += 3
        
    print(f"Your finalk bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride")
     
