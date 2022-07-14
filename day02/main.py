#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("Welcome to the tip calculator.")
bill= float(input("What was the total bill? $"))
tip= int(input("What tip percentage would you like to leave? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇
percent = tip / 100
total_tip = bill * percent
total = bill + total_tip
per_person = total / people
# final_amount= round(per_person,2)
final_amount="{:.2f}".format(per_person)
print(f"Each person should pay: ${final_amount}")
