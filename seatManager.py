
from heapq import *
class SeatManager:
    # 优先队列 堆

    def __init__(self, n: int):
        self.lt = []
        for i in range(n):
            self.lt.append( i +1)
        heapify(self.lt)

    def reserve(self) -> int:
        return heappop(self.lt)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.lt ,seatNumber)



if __name__ == '__main__':
    seatManager = SeatManager(5)
    print(seatManager.reserve())
    print(seatManager.reserve())
    seatManager.unreserve(1)