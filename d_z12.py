import random
list1 = [random.randint(0,5) for i in range(5)]
list2 = [random.randint(0,5) for i in range(5)]
result = [x for x in list1 if x in list2]
print(result)




