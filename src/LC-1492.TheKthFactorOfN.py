 class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        st = []
        end = deque([])
        if n % 2 == 0:
            for num in range(1, ceil(n**0.5)+1):
                if n % num == 0 and (not end or num < end[0]):
                    st.append(num)
                    if n//num != num:
                        end.appendleft(n//num)
        else:
            for num in range(1, ceil(n**0.5)+1, 2):
                if n % num == 0 and (not end or num < end[0]):
                    st.append(num)
                    if n//num != num:
                        end.appendleft(n//num)
        factors = st + list(end)
        return -1 if k > len(factors) else factors[k-1]