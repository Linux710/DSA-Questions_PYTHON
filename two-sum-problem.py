# Two Sum solution in O(n) using Dictionary 


#---------[ Two Sum Function ]-------------------------
def twoSum(nums,target):
     values = {}    # empty Dictionary
     for idx,value in enumerate(nums):
         if target-value in values:
             return [values[target-value],idx]
         else:
             values[value] = idx
#-------------[ End of Function ]-------------------------
myList  = [1,9,9,3,2]
v = 12

print(twoSum(myList,v)) // print
