

import heapq
if __name__ == '__main__':
    q = []
    mp = {}
    k = 3
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    for i in range(k):
        heapq.heappush(q, -nums[i])
        if -nums[i] not in mp:
            mp[-nums[i]] = 1
        else:
            mp[-nums[i]] += 1
    res = []
    top = heapq.heappop(q)
    res.append(-top)
    heapq.heappush(q, top)
    for i in range(k, len(nums)):
        if -nums[i] not in mp:
            mp[-nums[i]] = 1
        else:
            mp[-nums[i]] += 1
        mp[-nums[i - k]] -= 1
        heapq.heappush(q, -nums[i])
        curtop = heapq.heappop(q)
        heapq.heappush(q, curtop)
        while mp[curtop] <= 0:
            heapq.heappop(q)
            curtop = heapq.heappop(q)
            heapq.heappush(q, curtop)
        curtop = heapq.heappop(q)
        heapq.heappush(q, curtop)
        res.append(-curtop)
    print(res)
