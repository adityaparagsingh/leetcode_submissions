class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for str in strs:
            key = "".join(sorted(str))

            if key not in hashmap:
                hashmap[key] = []
            
            hashmap[key].append(str)
        return list(hashmap.values())
        