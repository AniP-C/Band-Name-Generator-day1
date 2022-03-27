print("Welcome to Pizza Hut, delivery system!")
size= input("What's the type of pizza you want? (Small) 'S', (Medium) 'M', (Large) 'L' ")
add_toppings = input("Do you want to add any topings ? 'Y' or 'N' ")
add_cheese = input("Do you want to add extra cheese? 'Y' or 'N' ")

bill =0

if size== 'S':
    bill= bill +15
elif size== 'M':
    bill = bill+20
elif size == 'L' :
    bill = bill + 25
else:
    bill = bill + 30

if add_toppings== 'Y':
    if size== 'S':
        bill = bill + 2
    else:
        bill = bill+ 3

if add_cheese== 'T':
    bill = bill +1

print(f" Your total bill amount is ${bill}")








    
