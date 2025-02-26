class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n == nums[i - 1] and i > 0:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = n + nums[l] + nums[r]
                if sum > 0:
                    r -=1
                elif sum < 0:
                    l += 1
                else:
                    res.append([n, nums[l], nums[r]])
                    r -= 1
                    l +=1
                    while nums[r] == nums[r+1] and l < r:
                        r -= 1
        return res
        
        # print(nums)
        





solution = Solution()



# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
print(f"the triplet are: {solution.threeSum([-1,0,1,2,-1,-4])}")

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
print(f"the triplet are: {solution.threeSum([0,1,1])}")


# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
print(f"the triplet are: {solution.threeSum([0,0,0])}")
 