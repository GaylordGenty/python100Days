#Write your code below this line 👇

def prime_checker(number) :
    
    for i in range(2,number+1) :
        if number % i == 0 and i != number:
            print("It's not a prime number.")
            break
        elif number % i == 0 and i == number :
            print("It's a prime number.")
            break

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
