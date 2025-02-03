class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numberCounter = {}
        for num in nums:
            if num in numberCounter:
                return True
            else:
                numberCounter[num] = 0
        return False


solution = Solution()

print(f"there are duplicate {solution.containsDuplicate([1,2,3,1])}")

print(f"there are duplicate {solution.containsDuplicate([1,2,3,4])}")

print(f"there are duplicate {solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])}")

