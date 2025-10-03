# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

# If the town judge exists, then:

# The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

from typing import List, Dict, Set

class Solution:

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # satisfy the conditions that the max count will be n-1,
        # the key of max count is not in the map
        trust_counts = {}
        uniq_keys = set()
        # fill in the counts
        for i in range(len(trust)):
            if trust[i][1] in trust_counts:
                trust_counts[trust[i][1]] += 1
            else:
                trust_counts[trust[i][1]] = 1
            
            uniq_keys.add(trust[i][0])
            
        # find max key, val
        max_c = 0
        max_id = -1
        for k, v in trust_counts.items():
            if v > max_c:
                max_id = k
                max_c = v
        
        # max key's count is n-1
        if max_c != n-1:
            return -1
        
        # check if the key exists in the list
        if max_id in uniq_keys:
            return -1
        return max_id