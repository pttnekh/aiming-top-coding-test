from collections import Counter

def solution(clothes):
    kind_count = Counter([cloth[1] for cloth in clothes])
    answer = 1
    for cnt in kind_count.values():
        answer *= (cnt+1)
    return answer - 1