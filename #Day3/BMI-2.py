print("More advanced BMI calculator")
weight= float(input("Enter your weight in kilograms (kgs) :"))
height= float(input("Enter your height in metres (m) :"))
bmi = weight/(height*height)
round (bmi, 2)
if bmi <18.5 :
    print(f"Your BMI is  {bmi} , which is under 18.5, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is  {bmi} , which is under 25, but above 18.5 which means you are of normal weight.")
elif bmi <30 :
    print(f"Your BMI is  {bmi} , which is under 30, but above 25 which means you are overweight.")
elif bmi <35:
    print(f"Your BMI is  {bmi} , which is under 35, but above 30 which means you are obese.")
elif bmi >35 :
    print(f"Your BMI is  {bmi} , which is above 35 which means you are critically obese.")