import copy 
def permuteUnique(nums):
    res = []
    permuteRecursive(nums,0,res)
    return res

def permuteRecursive(nums,begin,res):
    if begin >= len(nums)-1:
        num = copy.deepcopy(nums)
        res.append(num)
        return
    
    for i in range(begin,len(nums)):
        if begin!=i and nums[i]==nums[begin]:
            continue
        nums[begin], nums[i] = nums[i],nums[begin]
        permuteRecursive(nums,begin+1,res)
        nums[begin], nums[i] = nums[i],nums[begin]
 

            
        


        
    
    



print(permuteUnique([1,1,2]))
