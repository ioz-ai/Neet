# You are given an array of integers stones where stones[i] represents the weight of the ith stone.

# We want to run a simulation on the stones as follows:

# At each step we choose the two heaviest stones, with weight x and y and smash them togethers
# If x == y, both stones are destroyed
# If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# Continue the simulation until there is no more than one stone remaining.

# Return the weight of the last remaining stone or return 0 if none remain.


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        # 2. Run the simulation while there are at least two stones.
        while len(max_heap) > 1:
            # 3. Pop the two heaviest stones.
            # heappop returns the "smallest" item, which is the most negative,
            # so we negate it back to its positive weight.
            heavy1 = -heapq.heappop(max_heap)
            heavy2 = -heapq.heappop(max_heap)

            # 4. Smash them. If their weights are different,
            # push the new stone back onto the heap.
            if heavy1 > heavy2:
                new_weight = heavy1 - heavy2
                heapq.heappush(max_heap, -new_weight)
        
        # 5. After the loop, return the last stone's weight or 0.
        if not max_heap:
            return 0  # No stones left
        else:
            return -max_heap[0] # The one remaining stone