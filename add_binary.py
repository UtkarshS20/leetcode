def addBinary(a: str, b: str) -> str:
    i, j, carry = len(a)-1, len(b)-1, 0
    result = []
    while i>=0 or j>=0 or carry:
        carry += (0 if i<0 else int(a[i]))+(0 if j<0 else int(b[j]))
        carry, v = divmod(carry, 2)
        result.append(str(v))
        i, j = i-1, j-1
    return "".join(result[::-1]) 
    
    
# a = "11"
# b = "1"

a = "1010"
b = "1011"
print(addBinary(a=a, b=b))