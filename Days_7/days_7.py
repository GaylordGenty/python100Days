import random

word_list = ["aardvark", "baboon", "camel"]
blankWord = []
letterUse = []
liveBarre = ["❤️","❤️","❤️","❤️","❤️","❤️"]

randWord = random.choice(word_list)
randWordList = list(randWord)

index = 0
fail = 0
letterFind = 0
goodAnswer = False
gameFinish = False

for i in randWordList :
    blankWord.append("_")

print("***** New game *****")
print("".join(blankWord))

while gameFinish == False:

    if fail == 6 :
        print("""
              ******************
              * You loose ! :( *
              ******************
              """)
        break
    elif letterFind == len(randWordList) :
        print("""
              ****************
              * You win ! :) *
              ****************
              """)
        break
    else :
        chooseLetter = input("choose a letter\n").lower()
        letterUse.append(chooseLetter)
        letterUse.sort()

        for i in randWordList :
            if i == chooseLetter :
                blankWord[index] = chooseLetter
                letterFind +=1
                goodAnswer = True
            
            index +=1
        
        if goodAnswer == False :
            fail +=1

    for i in range(fail) :
        liveBarre[i] = "🖤"
    
    print(f"You have use the letters : {letterUse}")
    print(f"Live point {liveBarre}")
    print("".join(blankWord))
    index = 0
    goodAnswer = False


