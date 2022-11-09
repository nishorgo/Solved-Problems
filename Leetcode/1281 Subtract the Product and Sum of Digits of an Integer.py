def subtractProductAndSum(self, n: int) -> int:
        product = 1
        summation = 0
        
        while True:
            product *= n % 10
            summation += n % 10
            
            n = n // 10
            if n <= 0: break
        
        return product - summation