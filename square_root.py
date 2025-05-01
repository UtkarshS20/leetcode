def mySqrt(x: int) -> int:
    if x<=1:
        return x
    low = 1
    sq = low*low
    while (sq<=(x)):
        low=low+1
        sq = low*low
    return low-1
        
    # return (x ** 0.5)//1
    
# x = 4
x = 8
print(mySqrt(x))