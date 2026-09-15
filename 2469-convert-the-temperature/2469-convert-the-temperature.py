class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        k = celsius + 273.15
        f = celsius * 1.80 + 32.00
        arr = [0,0]
        arr[0] = k
        arr[1] = f
        return arr