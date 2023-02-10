# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇


col = int(position[0])-1
row = int(position[1])-1

print("map",map[row][col])
map[row][col] = "X"

# if row == 0:
#     row1[col] = "X"
# elif row == 1:
#     row2[col] = "X"
# else:
#     row3[col] = "X"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")