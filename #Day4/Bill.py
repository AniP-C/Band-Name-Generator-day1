import random
test_seed = int(input(" Create a seed number "))
random.seed(test_seed)

namsAsCSV = input("Give everybody's names separated by a comma.")
names=namsAsCSV.split(", ")

names_len = len(names)
random_number = random.randint(0, names_len-1)
person_will_pay = names[random_number]
print(f"{person_will_pay} will pay for the food today")