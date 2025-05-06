def climbStairs(n: int) -> int:
    a, b = 0,1
    for i in range(n):
        a,b= b, a+b
    return b

n = 4
print(climbStairs(n))