def solution(arr):
    q = []
    for i in arr:
        if not q or q[-1] != i:
            q.append(i)
            
    return q