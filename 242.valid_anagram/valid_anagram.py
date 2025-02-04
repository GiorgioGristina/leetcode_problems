class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

# better solution with O(n) TC

        # dictT ={}
        # for c in t:
        #     if c in dictT:
        #         dictT[c] += 1 
        #     else:
        #      dictT[c] = 1 
        # print(f"T dic is : {dictT}")
        # dictS= {}
        # for c in s:
        #     if c in dictS:
        #         dictS[c] += 1 
        #     else: 
        #         dictS[c] = 1 
        # print(f"S dic is : {dictS}")

        # return dictT == dictS


# cleaned up solution avoiding using the 2 dictionary

        charCount = {}

        for c in s:
            charCount[c] = charCount.get(c, 0) + 1

        for c in t:
            if charCount.get(c, 0) > 0:
                charCount[c] -= 0
            else:
                return False
        return True

# sorting solution less efficient with n log(n) TC

        # sortedSString = sorted(s)
        # sortedTString = sorted(t)

        # return sortedSString == sortedTString 

instance = Solution()
# s = "anagram", t = "anagram" 
print(f"is an anagram: {instance.isAnagram('anagram',  'anagram')}")

# s = "rat", t = "car"
print(f"is an anagram: {instance.isAnagram('rat',  'car')}")
