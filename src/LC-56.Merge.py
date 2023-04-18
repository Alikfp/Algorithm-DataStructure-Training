class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intvs = sorted(intervals, key = lambda x : x[0])

        mn, mx = intvs[0][0], intvs[0][1]
        i = 1
        # iterate through intervals
        while i < len(intvs):
            #print(res)
            st, end = intvs[i][0], intvs[i][1]

            # can merge
            if mx >= st :
                mx = max(end, mx)

            else:
                res.append([mn, mx])
                mn, mx = st, end
            
            i += 1
        
        return res + [[mn, mx]]