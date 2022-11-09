def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(31, -1, -1):
            if n & (1 << i):
                count += 1
                
        return count