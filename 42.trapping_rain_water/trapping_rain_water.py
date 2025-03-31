class Solution:
    def trap(self, height: list[int]) -> int:

        # Solution with TC O(n) SC O(n)

        # res = 0
        # length = len(height)
        # max_left = [0] * length
        # max_right = [0] * length
        # max_l = 0
        # max_r = 0
        # for i in range(0, length):
        #     if i == 0:
        #         max_left[i] = 0
        #     else:
        #         max_left[i] = max(max_left[i - 1], height[i - 1])

        # for i in range(length -1, -1, -1):
        #     if i == length - 1:
        #         max_right[i] = 0
        #     else:
        #         max_right[i] = max(max_right[i + 1], height[i + 1])

        # for i in range(0, length):
        #     amount = min(max_left[i], max_right[i]) - height[i]
        #     if amount < 0:
        #         res += 0
        #     else:
        #         res += amount
        # return res

# Solution with TC O(n) SC O(1)

        res = 0
        l = 0
        r = len(height) -1
        max_l = height[l]
        max_r = height[r]

        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                res += max_l - height[l]
            else:
                r -=1
                max_r = max(max_r, height[r])

                res += max_r - height[r]

        return res







solution = Solution()

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))

# Input: height = [4,2,0,3,2,5]
# Output: 9

print(solution.trap([4,2,0,3,2,5]))
