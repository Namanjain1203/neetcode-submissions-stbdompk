class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
            
        total_tank = 0
        current_tank = 0
        start = 0

        for i in range(len(gas)):
            gain = gas[i] - cost[i]
            total_tank += gain
            current_tank += gain

            # If we run out of gas, reset start
            if current_tank < 0:
                start = i + 1
                current_tank = 0

        # If total gas is enough, return start index
        return start if total_tank >= 0 else -1