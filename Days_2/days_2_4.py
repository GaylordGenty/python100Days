#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

nb_ppl = int(input("How many ppl ?\n"))
amount_bill = float(input("Amount of the bill ?\n"))
amount_tips = int(input("Amount of the tips on %\n"))

def tipsCalc(ppl,bill,tips) :
    return round((amount_bill / nb_ppl) * ((amount_tips / 100)+1),2)

print(f"The amount of the tips is {tipsCalc(nb_ppl,amount_bill,amount_tips)}")