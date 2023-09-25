# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

index = 0
somme = 0

# print(type(two_digit_number))
# int(two_digit_number)

while index < len(two_digit_number) :
    somme += int(two_digit_number[index])
    index += 1

print(somme)