# Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.
# Implement the following methods:
# constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
# int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.

import heapq
from typing import List

class KthLargest:
    """
    KthLargest implementation using a Min-Heap.
    """
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums
        
        heapq.heapify(self.min_heap) 
        
        # Prune the heap: keep only the k largest elements
        # This is the most efficient way to initialize the top k elements.
        while len(self.min_heap) > k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        # 1. If the heap is not yet full, just push the new value.
        # This is correct and keeps the heap small.
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        
        # 2. If the heap is full AND the new value is larger than the smallest element
        # (the root, which is the current k-th largest), replace the smallest.
        elif val > self.min_heap[0]:
            # This is O(log k) and ensures the heap size remains k
            heapq.heappushpop(self.min_heap, val)
            
        # The k-th largest element is always the smallest in the min-heap (at index 0)
        # This assumes the heap is not empty, which it must be after initialization or first push.
        return self.min_heap[0]
