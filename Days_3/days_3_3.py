# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

def leapNoLeap(y) :
    return y % 4

if leapNoLeap(year) % 4 == 0 :
    print("Leap year")
else :
    print("Not leap year.")


