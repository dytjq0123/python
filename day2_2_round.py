# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#rint((int(weight) % float(height) ** 2))
#print(round(int(weight) / float(height) ** 2))

result = round(float(weight) / float(height) ** 2, 1)

if result < 18.5:
    print(f"Your BMI is {result}, you are underweight.")
elif result < 25:
    print(f"Your BMI is {result}, you are normal weight.")    
elif result < 30:
    print(f"Your BMI is {result}, you are slightly overweight.")    
elif result < 35: 
    print(f"Your BMI is {result}, you are obese.")    
else:
    print(f"Your BMI is {result}, you are clinically obese.")            