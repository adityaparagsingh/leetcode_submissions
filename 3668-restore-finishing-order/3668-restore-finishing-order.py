class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        arr = []
        for i in range(len(order)):
            for j in range(len(friends)):
                if order[i]==friends[j]:
                    arr.append(friends[j])
        return arr