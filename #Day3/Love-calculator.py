from traceback import print_tb


print("Welcome to Love calculator !")
name1 = input("Enter your name")
name2 = input("Enter your partner's name")

combined_name = name1 + name2

combined_name_lowercase = combined_name.lower()

t= combined_name_lowercase.count("t")
r= combined_name_lowercase.count("r")
u= combined_name_lowercase.count("u")
e= combined_name_lowercase.count("e")

total_trueness = t +r+u+e

l= combined_name_lowercase.count("l")
o= combined_name_lowercase.count("o")
v= combined_name_lowercase.count("v")
e= combined_name_lowercase.count("e")
total_love= l+o+v+e

combined_result = str(total_love) + str(total_trueness)
int_combined_result = int(combined_result)
if int_combined_result < 10 or int_combined_result > 90  :
    print(f"Your love percentage is {int_combined_result}% , you are like mentos in cola")
elif int_combined_result < 50 and int_combined_result > 40 :
    print(f"Your love percentage is {int_combined_result}% , you good to go")
else :
    print(f"Your love score is {int_combined_result}")