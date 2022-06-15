#   Welcome the user
print("Welcome to my tip calculator!")
# Ask for the total bill
bill=float(input("What was the total bill? $"))
# Ask what % of tip there would like to give
tip=float(input("What percentage of tip would you like to give? 10, 12, 15...? "))
# Ask for the available people involve in the split
people_for_split= int((input("How many people to split the bill? ")))
# Do some magic... Whooooshhh
percentage_bill= (bill*(100/tip))
#Calculate the total bill after the tip
total_bill= (bill+percentage_bill)
each_person_to_pay= total_bill/people_for_split
rounded_value= round(each_person_to_pay,2)
# Final amount with no approximation
print(f"Each person to pay: {each_person_to_pay}")
# Round the answer to two significant figures
print(f"Each person to pay: {rounded_value}")
