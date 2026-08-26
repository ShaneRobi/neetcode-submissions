class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set(nums)
        longest = 0 

        for num in number_set:
            if num - 1 not in number_set:
                current_length = 1
            
                while num + current_length in number_set:
                    current_length += 1
                
                longest = max(longest, current_length)

        return longest
