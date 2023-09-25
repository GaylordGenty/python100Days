#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇

import random
randomInt = random.randint(0,1)

if randomInt == 0 :
    print("Tails")
elif randomInt == 1 :
    print("Heads")