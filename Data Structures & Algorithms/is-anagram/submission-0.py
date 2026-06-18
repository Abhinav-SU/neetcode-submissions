class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first check the length of both the string and if not same return false
        #so one approach is either just sort both strings and compare each char in both
        #string if not equal at any point then return false otherwise continue
        #this approach is nlogn but doesnt require extra space
        #other approach is to keep freq map of both string and go over them and check if 
        #they are same
        n = len(s)
        m = len(t)
        if n !=m:
            return False

        s= "".join(sorted(s))
        t= "".join(sorted(t))

        for i in range(0,n):
            if s[i] != t[i]:
                return False
        return True
        