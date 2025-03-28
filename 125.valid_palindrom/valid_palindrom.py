class Solution:
    def isPalindrome(self, s: str) -> bool:  
        if len(s) == 0:
            return True      
        left, right = 0, len(s) - 1

        while left < right:
            while not s[left].isalnum() and left < right:
                left += 1
            while not s[right].isalnum() and left < right:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True



solution = Solution()

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
print(f"is a palindrome? {solution.isPalindrome('A man, a plan, a canal: Panama')}")


# Input: s = "race a car"
# Output: false
print(f"is a palindrome? {solution.isPalindrome('race a car')}")


# Input: s = " "
# Output: true
print(f"is a palindrome? {solution.isPalindrome(' ')}")