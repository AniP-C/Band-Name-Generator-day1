from asyncio import run_coroutine_threadsafe


height = input ( " Enter your height in metres (m) :")
weight = input("Enter your wieght in kiligrams (kgs) :")

bmi= float(weight)/ float(height*height)
round(bmi, 2)

print(f"Your Body Mass Index (BMI) is : {bmi}")