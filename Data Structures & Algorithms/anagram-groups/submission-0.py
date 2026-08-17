class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        res = defaultdict(list) # mapping charCount to list of anagrams

        for s in strs: 
            count = [0] * 26 # one for each character

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())