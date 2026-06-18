class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #sort the list
        #check if the element next is same as curr if yes return true else false
        #sorting is nlogn 
        #use hashset store numbers one by one if cant then duplicate exist return true else false
        map = set()
        n = len(nums)
        if n == 0: return False 
        for num in nums:
            if num not in map:
                map.add(num)
            else:
                return True

        return False
        