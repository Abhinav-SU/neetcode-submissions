from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    #add each elem and its index to a dict
        #check if the target - currElem exit in the dict 
        #if yes return the index of both the complement and the currElem
        #if not move forward 

        map = defaultdict(int)

        for i,num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [map.get(complement),i]
            map[num] = i

        return []
        