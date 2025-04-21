from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    if target not in nums and target > nums[-1]:
        return len(nums)
    for index in range(len(nums)):
        if nums[index] == target:
            return index
        elif nums[index] > target:
            return index 
    
# nums = [1,3,5,6]
# target = 5
# nums = [1,3,5,6]
# target = 2
# nums = [1,3,5,6]
# target = 7
# print(searchInsert(nums=nums, target=target))
