class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r

        while l <= r:
            mid = l + (r - l) // 2
            hours = 0
            for pile in piles:
                hours += (pile + mid -1)// mid

            if hours <= h:
                ans = mid
                r = mid - 1 
            else:
                l = mid + 1
        return ans

        