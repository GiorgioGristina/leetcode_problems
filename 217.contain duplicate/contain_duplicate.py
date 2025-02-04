class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numberCounter = {}
        for num in nums:
            if num in numberCounter:
                return True
            else:
                numberCounter[num] = 0
        return False


# Set lenght evaluation against nums list

# class Solution:
# def containsDuplicate(nums: list[int]) -> bool:
#     return len(nums) != len(set(nums))


# Use Set because is more memory efficient

# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False

solution = Solution()

print(f"there are duplicate {solution.containsDuplicate([1,2,3,1])}")

print(f"there are duplicate {solution.containsDuplicate([1,2,3,4])}")

print(f"there are duplicate {solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2])}")

