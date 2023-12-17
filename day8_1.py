#Write your code below this line 👇
import math


def paint_calc(height, width, cover):
    hxw = int(height) * int(width)
    value = hxw / cover
    
    # value = int(value)
        
    # value = math.floor(hxw / cover)
    # if hxw % cover != 0: 
    #     value += 1
    
    value = math.ceil(value)
            
    print(f"You'll need {value} cans of paint.")






#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


