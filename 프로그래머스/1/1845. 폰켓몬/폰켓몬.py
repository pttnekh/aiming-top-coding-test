from collections import Counter

def solution(nums):
    
    pick = len(nums) // 2 
    num = len(set(nums))
    
    return min(pick, num)

              