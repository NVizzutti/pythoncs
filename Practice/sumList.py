import math

def sumList(list1):
    Sum=0
    i=0
    while i<len(list1):
        Sum=Sum+list1[i]
        i=i+1
    return Sum

numbers=[6,2,5,7]
Sum=sumList(numbers)
print Sum

List2=[9,2,5,6,7,1]
Total=sumList(List2)
print Total

