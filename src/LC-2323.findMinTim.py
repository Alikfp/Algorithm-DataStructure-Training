class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        srt_jbs = sorted(jobs)
        srt_wrks = sorted(workers)
        mx_days = 0
        for i in range(len(jobs)):
            mx_days = max(srt_jbs[i]/srt_wrks[i], mx_days)
        return math.ceil(mx_days)
        



