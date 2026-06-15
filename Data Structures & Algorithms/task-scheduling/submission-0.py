from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        Maxfreg = max(count.values())

        Maxcounter = sum(1  for i in count.values() if i == Maxfreg )

        return max(len(tasks), (Maxfreg - 1) * (n + 1) + Maxcounter)

        