
class UndergroundSystem:

    def __init__(self):
        self.st = {}
        self.ct = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        tmp = str(stationName)+'#'+str(t)
        self.st[id] = tmp

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        val = self.st[id]
        val = val.split('#')
        s = val[0]+'#'+stationName
        if s not in self.ct:
            self.ct[s] = str(t-int(val[1]))+'#'+'1'
        else:
            tmp = self.ct[s].split('#')
            self.ct[s] = str(int(tmp[0])+t-int(val[1]))+'#'+str(int(tmp[1])+1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        tmp = startStation+'#'+endStation
        val = self.ct[tmp]
        val = val.split('#')
        return int(val[0])/int(val[1])






# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)