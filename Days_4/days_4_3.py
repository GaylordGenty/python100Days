# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

if position != "" :
    collone = int(position[0])
    ligne = int(position[1])
    listeDeListe = [row1, row2, row3]
    if collone >= 1 and collone <=3 and ligne >= 1 and ligne <= 3 :
        collone -= 1
        ligne -= 1
        listeDeListe[ligne][collone] = "X"



#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

