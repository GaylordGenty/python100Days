# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maxScore = 0

for i in range(len(student_scores)) :
    if student_scores[i] > maxScore :
        maxScore = student_scores[i]

print(f"The highest score in the class is: {maxScore}")



