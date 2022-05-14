# import random

# random_int=random.randint(1,20)
# print(random_int)

# random_float = random.random()
# random_float= 5*random_float
# print(random_float)



my_list = ["appple", "banana", "orange", "almond"]
my_list1= ["scorpio", "skoda", "honda city", "audi"]
my_list2= ["12", "123","12432","12333"]

my_combined_list =[my_list1,my_list,my_list2]
print(f"{my_list}\n {my_list1}\n {my_list2}")

position_from_user = input("Enter your position")

horizontal_position = int(position_from_user[0])
vertical_position = int(position_from_user[1])

select_a_row = my_combined_list[vertical_position-1]
select_a_row[horizontal_position-1] = 'XX'

print(f"{my_list}\n {my_list1}\n {my_list2}")




