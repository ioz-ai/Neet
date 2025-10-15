# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

from typing import List
from collections import Counter

class Solution:
    class E:
        def __init__(self, item, count):
            self.item = item
            self.count = count

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count
        c = {}
        for i in nums:
            c[i] = c.get(i, 0) + 1

        elems = []
        for key, value in c.items():
            elems.append(self.E(key, value))
        # sort desc
        sorted_by_c = sorted(elems, key=lambda e: e.count, reverse=True)
        # get top k
        return [elem.item for elem in sorted_by_c[:k]]