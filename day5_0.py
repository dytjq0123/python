# 🚨 Don't change the code below 👇
# student_heights = input("Input a list of student heights ").split(", ")
# student_heights = "180, 124, 165, 173, 189, 169, 146".split(", ")
student_heights = "156, 178, 165, 171, 187".split(", ")
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
result = sum(student_heights) / len(student_heights)
print(round(result))

print(max(student_heights))


