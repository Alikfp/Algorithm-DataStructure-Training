class Solution:
    def minSwaps(self, data: List[int]) -> int:
        domain = sum(data)
        # get the domain with max sum
        
        curr_sum = sum(data[0:domain])
        i, j = 1, domain
        max_sum = curr_sum
        while j < len(data):
            curr_sum += (-data[i-1] + data[j])
            max_sum = max(max_sum, curr_sum)
            i += 1
            j += 1
        return domain-max_sum