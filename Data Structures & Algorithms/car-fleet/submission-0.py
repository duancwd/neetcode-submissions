class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car = sorted(zip(position,speed))
        fleet = 0
        last = 0

        for p, s in reversed(car):
            time = (target - p) / s

            if time > last:
                fleet += 1
                last = time
        return fleet
        