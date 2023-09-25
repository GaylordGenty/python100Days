# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
rightNumber = int(0)
rightWord = "LOVE"

leftNumber = int(0)
leftWord = "TRUE"

name3 = str(name1+""+name2)

for i in range(len(rightWord)) :
    #print(str(rightWord[int(i)]))
    rightNumber += name3.upper().count(rightWord[int(i)])

for i in range(len(leftWord)) :
    leftNumber
    leftNumber += name3.upper().count(leftWord[int(i)])

trueLoveMetter = int(f"{leftNumber}{rightNumber}")

if trueLoveMetter < 10 or trueLoveMetter > 90 :
    print(f"Your score is {trueLoveMetter}, you go together like coke and mentos.")
elif trueLoveMetter >= 40 and trueLoveMetter <= 50 :
    print(f"Your score is {trueLoveMetter}, you are alright together.") 
else :
    print(f"Your score is {trueLoveMetter}.")