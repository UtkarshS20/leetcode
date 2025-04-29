from typing import List


def plusOne(digits: List[int]) -> List[int]:
    for i in range(len(digits)-1,-1,-1):
        print(digits[i])
        # return i
        if digits[i] != 9:
            digits[i] = digits[i]+1
            return digits
        else:# digits[i] == 9:
            digits[i] = 0
            # continue
    if digits[0] == 0:
        return [1]+ digits
    return digits
        
    
    
digits = [1,2,3]
# digits = [4,3,2,1]
# digits = [9,9]
print(plusOne(digits))