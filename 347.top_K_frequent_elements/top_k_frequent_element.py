from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        highest_frequency = []
        frequency_tracker = defaultdict(int)
        # track frequency
        for n in nums:
            frequency_tracker[n] += 1
        # get the K highest frequency
        print(frequency_tracker)
        i=0
        while i < k:
            key = max(frequency_tracker, key= lambda k: frequency_tracker[k])
            highest_frequency.append(key)
            frequency_tracker.pop(key)
            print(key)
            i+=1
        return highest_frequency


solution = Solution()

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
print(f"the 2 more frequent nums are: {solution.topKFrequent([1,1,1,2,2,3], 2)}")

# Input: nums = [1], k = 1
# Output: [1]
print(f"the 1 more frequent nums are: {solution.topKFrequent([1], 1)}") 


