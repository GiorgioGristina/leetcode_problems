class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

# better solution with O(n) TC

        dictT ={}
        for c in t:
            if c in dictT:
                dictT[c] += 1 
            else:
             dictT[c] = 1 
        print(f"T dic is : {dictT}")
        dictS= {}
        for c in s:
            if c in dictS:
                dictS[c] += 1 
            else: 
                dictS[c] = 1 
        print(f"S dic is : {dictS}")

        return dictT == dictS


# sorting solution less efficient with n log(n) TC

        # sortedSString = sorted(s)
        # sortedTString = sorted(t)

        # return sortedSString == sortedTString 

