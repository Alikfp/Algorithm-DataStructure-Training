class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tank = 0
        st = 0
        total = 0

        for i in range(n):
            total += (gas[i] - cost[i])
            tank += (gas[i] - cost[i])
            if tank < 0:
                tank = 0
                st = i+1
        return st if total>=0 else -1