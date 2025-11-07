import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        freqMap = {}

        for num in nums:
            if num not in freqMap:
                freqMap[num] = 0
            freqMap[num] += 1

        heap = []

        for num, freq in freqMap.items():
            if len(heap) <= k:
                heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
            
        res = [num for (freq, num) in heap]

        return res

        