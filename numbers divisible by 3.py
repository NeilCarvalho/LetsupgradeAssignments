vals = [int(i) for i in input("please enter a list of numbers:").split()]
#print(type(vals))
#print(len(vals))
#print(type(len(vals))
numbers_divisible_by3 = []
i = 0
k = int(len(vals))
while i < k:
    if vals[i] % 3 == 0:
        numbers_divisible_by3.append(vals[i])
    i = i + 1
print("The numbers entered that are divisible by 3 are", numbers_divisible_by3)
