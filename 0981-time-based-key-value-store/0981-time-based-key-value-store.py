from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        t_store = self.map.get(key, [])
        low, high = 0, len(t_store) - 1
        
        while low <= high:
            mid = (low + high) >> 1
            if t_store[mid][0] <= timestamp:
                res = t_store[mid][1]
                low = mid + 1
            else:
                high = mid - 1
        
        return res