class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n = len(dist)
        times = [(dist[i] - 1) // speed[i] for i in range(n)]
        times.sort()
        return next((i for i in range(n) if times[i] < i), n)
