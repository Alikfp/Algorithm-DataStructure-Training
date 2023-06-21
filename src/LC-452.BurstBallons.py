class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        srt_blls = sorted(points, key=lambda x : x[1])
        shots = 0
        last_shot = float("-inf")
        for st, end in srt_blls:
            if st > last_shot:
                # shoot
                last_shot = end
                shots += 1
        return shots