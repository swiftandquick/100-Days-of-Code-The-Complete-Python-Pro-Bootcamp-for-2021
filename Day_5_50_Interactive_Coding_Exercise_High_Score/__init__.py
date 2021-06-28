# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Set initial high score equal to first index.
high_score = student_scores[0]

# If score > high_score, set it as new high_score.
for score in student_scores:
  if score > high_score:
    high_score = score

print(high_score)
