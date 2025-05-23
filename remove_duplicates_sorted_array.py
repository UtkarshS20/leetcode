from typing import List

def removeDuplicates(nums: List[int]) -> int:

    if not nums:
        return 0
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j = j+1
            nums[j] = nums[i]
    return j+1

nums = [1,1,2]
print(removeDuplicates(nums))