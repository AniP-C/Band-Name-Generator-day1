total = 0
for even_num in range(2,101,2):
    total= even_num+ total
print(total)
    

# ################## ALTERNATIVE #######################
total2 = 0 
for e_num in range (1,101):
    if e_num%2 == 0:
        total2=e_num+total2
print(total2)