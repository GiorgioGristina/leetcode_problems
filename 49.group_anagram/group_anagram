from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        words_anagram = defaultdict(list)
        
        
        # my solution nk log^k using sorting

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in words_anagram:
                words_anagram[sorted_word].append(word)
            else:
                words_anagram[sorted_word] = [word]
        return list(words_anagram.values())

        #most efficent solution with O(kn) with frequency   


        # for word in strs:
        #     char_tracker = [0] * 26
        #     for char in word:
        #         print(f"the unicode for the char is: {ord(char) } and  it will be set at index: {ord(char) - ord('a')}")
        #         char_tracker[ord(char) - ord("a")] += 1
        #     print(f"creating 26 char list with frequency: {char_tracker}")
        #     words_anagram[tuple(char_tracker)].append(word)
        # return list(words_anagram.values())



solution = Solution()

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

print(f"the list of group anagram is: {solution.groupAnagrams(['eat','tea','tan','ate','nat','bat'])}")

# Input: strs = [""]

# Output: [[""]]

print(f"the list of group anagram is: {solution.groupAnagrams([''])}")

# Input: strs = ["a"]

# Output: [["a"]]

print(f"the list of group anagram is: {solution.groupAnagrams(['a'])}")
