```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        min_que = []
        for i in range(len(arr)):
            heapq.heappush(min_que, -arr[i])
            if len(min_que) > k:
                heapq.heappop(min_que)
        
        res = []
        for i in range(k-1, -1, -1):
            res.append(-heapq.heappop(min_que))
        return res
```
