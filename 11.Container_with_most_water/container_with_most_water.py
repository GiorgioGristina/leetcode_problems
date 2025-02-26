class Solution:
    def maxArea(self, height: list[int]) -> int:
        biggest_area = 0
        l,r = 0, len(height) -1

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            biggest_area = max(biggest_area, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return biggest_area

solution = Solution()



# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
print(f"the bigghet area is: {solution.maxArea([1,8,6,2,5,4,8,3,7])}")

# Input: height = [1,1]
# Output: 1
print(f"the bigghet area is: {solution.maxArea([1,1])}")

 