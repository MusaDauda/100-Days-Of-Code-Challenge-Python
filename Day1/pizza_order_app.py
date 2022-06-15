# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill=0
# Small Pizza: $15
if size=="S":
  bill+=15
  #Pepperoni for Small Pizza: +$2
  if add_pepperoni=="Y":
    bill+=2
  #Medium Pizza: $20
elif size=="M":
  bill+=20
  #Pepperoni for Medium or Large Pizza: +$3
  if add_pepperoni=="Y":
    bill+=3
  #Large Pizza: $25
elif size=="L":
  bill+=25
  #Pepperoni for Medium or Large Pizza: +$3
  if add_pepperoni=="Y":
    bill+=3
  #Extra cheese for any size pizza: + $1
if extra_cheese=="Y":
    bill+=1
else:
  #Invalidate the user if the wrong input is inserted
  print("Invalid Response")
print(f"Your total bill adds up to ${bill}")