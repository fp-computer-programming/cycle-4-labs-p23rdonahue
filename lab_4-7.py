#author: RED 10/19/22
#input statements
numbnumb1 = input("What is your first numbnumb?")
numbnumb2 = input("What is your second numbnumb?")
numbnumb3 = input("What is yo third number fool?")
numbnumb4 = input("What is yo fourth number bro?")
numbnumb5 = input("What is yo fifth number homeslice?")
#Change to int
uno = int(numbnumb1)
dos= int(numbnumb2)
tres= int(numbnumb3)
cuatro= int(numbnumb4)
cinco= int(numbnumb5)
#make one string and print
num_str= (numbnumb1 + ' ' + numbnumb2 + ' ' + numbnumb3 + ' ' + numbnumb4 + ' '+ numbnumb5)
print(num_str)
#if statements for larger num
if uno>dos:
    nah=uno
elif uno>tres:
    nah=uno
elif uno>cuatro:
    nah=uno
elif uno>cinco:
    nah=uno
else:
    biggest_num = uno

if dos>uno:
    nah= uno
elif dos>tres:
    nah=uno
elif dos>cuatro:
    nah=uno
elif dos>cinco:
    nah=uno
else: 
    biggest_num = dos

if tres>dos:
    nah=uno
elif tres>uno:
    nah=uno
elif tres>cuatro:
    nah=uno
elif tres>cinco:
    nah=uno
else:
    biggest_num = tres
if cuatro>dos:
    nah=uno
elif cuatro>uno:
    nah=uno
elif cuatro>tres:
    nah=uno
elif cuatro>cinco:
    nah=uno
else: 
    biggest_num = cuatro
if cinco>dos:
    nah=uno
elif cinco>uno:
    nah=uno
elif cinco>tres:
    nah=uno
elif cinco>cuatro:
    nah=uno
else:
    biggest_num = cinco
#if statements for smallest num
if uno<dos:
    nah=uno
elif uno<tres:
    nah=uno
elif uno<cuatro:
    nah=uno
elif uno<cinco:
    nah=uno
else:
    smallest_num = uno

if dos<uno:
    nah= uno
elif dos<tres:
    nah=uno
elif dos<cuatro:
    nah=uno
elif dos<cinco:
    nah=uno
else: 
    smallest_num = dos

if tres<dos:
    nah=uno
elif tres<uno:
    nah=uno
elif tres<cuatro:
    nah=uno
elif tres<cinco:
    nah=uno
else:
    smallest_num = tres
if cuatro<dos:
    nah=uno
elif cuatro<uno:
    nah=uno
elif cuatro<tres:
    nah=uno
elif cuatro<cinco:
    nah=uno
else: 
    smallest_num = cuatro
if cinco<dos:
    nah=uno
elif cinco<uno:
    nah=uno
elif cinco<tres:
    nah=uno
elif cinco<cuatro:
    nah=uno
else:
    smallest_num = cinco
#printing
print(biggest_num)
print(smallest_num)
print(smallest_num * biggest_num)