# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
# sum of the heights divide by number of entries give us the average.
average = int(round(sum(student_heights) / len(student_heights)))

print(f"{average}")
