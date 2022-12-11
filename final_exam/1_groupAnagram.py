from collections import List, defaultdict

class Solution:
    #given a strs
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        graph = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))
            graph[key].append(s)
            #every key-value stores the grouped anagrams

        return list(graph.values())
    #time complexity: O(N)
    #space complexity: O(N+MlogM) [mlogm is sorting in hashmap]