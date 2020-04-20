class Solution(object):
    def twoSum(self, nums, target):
        hashmap={}
        for m,x in enumerate(nums):
            hashmap[x]=m
        for n,y in enumerate(nums):
            j = hashmap[target-y]
            if j is not None and j!= n:
                return[n,j]

p = [3,2,4]
t = 6
r = Solution()
print(r.twoSum(p,t))