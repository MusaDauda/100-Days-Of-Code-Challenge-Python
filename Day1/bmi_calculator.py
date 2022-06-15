# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Under 18.5 they are underweight
bmi= round(weight/(height**2))
if (bmi<18.5):
  print(f"Your BMI is {bmi}, you are", '\033[1m' + 'underweight' + '\033[0m')
#Over 18.5 but below 25 they have a normal weight
elif (bmi<25):
  print(f"Your BMI is {bmi}, you have a", '\033[1m' + 'normal weight' + '\033[0m')
#Over 25 but below 30 they are slightly overweight
elif bmi<30:
  print(f"Your BMI is {bmi}, you are", '\033[1m' + 'slightly overweight' + '\033[0m')
#Over 30 but below 35 they are obese
elif bmi<35:
  print(f"Your BMI is {bmi}, you are", '\033[1m' + 'obese' + '\033[0m')
  # Above 35 they are clinically obese, in bold
else:
  print(f"Your BMI is {bmi}, you are",'\033[1m' + 'clinically obese' + '\033[0m')
# This is how to make a text bold using ANSI escape sequences
# '\033[1m' + 'Python' + '\033[0m'


1.64
