class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # declare de default dict of set
        tracker = {}
        longest = 0
        # loop throuh the array
        for n in nums:
            if n not in tracker:
                left = tracker.get(n -1, 0)
                right = tracker.get(n + 1, 0)
                total_length = left + 1 + right

                tracker[n] = total_length
                tracker[n - left] = total_length
                tracker[n + right] = total_length
            
                longest = max(longest, total_length )
        return longest


solution = Solution()


# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

print(f"the longest sequence is: {solution.longestConsecutive([100,4,200,1,3,2])}")

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
print(f"the longest sequence is: {solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1])}")

# Input: nums = [1,0,1,2]
# Output: 3
print(f"the longest sequence is: {solution.longestConsecutive([1,0,1,2])}")
