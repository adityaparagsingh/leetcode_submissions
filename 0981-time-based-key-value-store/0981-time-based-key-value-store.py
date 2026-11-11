class TimeMap:
    def __init__(self):
        self.keys: list[str] = []
        self.vals: list[str] = []
        self.stamps: list[list[tuple[int, int]]] = []

    def set(self, key: str, value: str, timestamp: int) -> None:
        if value not in self.vals:
            self.vals.append(value)
        v = self.vals.index(value)
        if key not in self.keys:
            self.keys.append(key)
            self.stamps.append([])
        row = self.stamps[self.keys.index(key)]
        if not row or row[-1][1] != v:
            row.append((timestamp, v))

    def get(self, key: str, timestamp: int) -> str:
        row = next((r for k, r in zip(self.keys, self.stamps) if k == key), [])
        return ([self.vals[v] for t, v in row if t <= timestamp] or [""])[-1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)