class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_position = sorted([(p,s) for p,s in zip(position,speed)], key = lambda t: -t[0])
        car_time = [(target - p)/s for p , s in sorted_position]

        fleet_count = 0
        last_fleet_time = 0 

        for time in car_time:
            if time>last_fleet_time:
                fleet_count +=1
                last_fleet_time = time
            else:
                fleet_count +=0
        return fleet_count