class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1= -heapq.heappop(stones) # O(logn)
            stone2= -heapq.heappop(stones) # O(logn)

            if stone2 == stone1:
                continue
            elif stone1 > stone2:
                heapq.heappush(stones,-(stone1-stone2))        
            else:
                heapq.heappush(stones,-(stone2-stone1))

        return -stones[0] if stones else 0

        