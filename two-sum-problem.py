# Two Sum solution in O(n) using Enumerate Function (Key-Value Pair data structure like dictionary)


#---------[ Two Sum Function ]-------------------------
def twoSum(nums,target):
     values = {}
     for idx,value in enumerate(nums):
         if target-value in values:
             return [values[target-value],idx]
         else:
             values[value] = idx
#-------------[ End of Function ]------------------------
myList  = [1,9,9,3,2]
t = 12

print(twoSum(myList,t))
