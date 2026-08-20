class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}  # stores each number and how many times it appears

        for num in nums:
            if num in freq:
                freq[num] += 1  # if we've seen it before, increase the count
            else:
                freq[num] = 1   # first time seeing it, start count at 1

        buckets = [[] for _ in range(len(nums) + 1)]
        # index = frequency
        # value = numbers that have that frequency

        for num, count in freq.items():
            buckets[count].append(num)
            # example: if num = 5 and count = 7
            # put 5 inside buckets[7]

        res = []  # stores the final top k frequent numbers

        for count in range(len(buckets) - 1, 0, -1):
            # start from the highest possible frequency
            # then move backwards: 10, 9, 8, 7...

            for num in buckets[count]:
                # look at every number inside this frequency bucket

                res.append(num)
                # add that number to our answer list

                if len(res) == k:
                    # once we have collected k numbers, we're done

                    return res