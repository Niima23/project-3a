#Amiin Samatar
#niima23
#10/11/22
#Finding the min and max values

print("How many integers would you like to enter?")
var = int(input())

print("please enter", var ,"integers.")
for x in range(0, var):
    num_1 = int(input())
    if x == 0:
        small = num_1
        large = num_1
    if num_1 < small:
        small = num_1
    if num_1 > large:
        large = num_1
print("min", small)
print("max", large)
