def pares_ate(n:int):
        return (i for i in range(2, n+1) if i % 2 == 0)