def solution(arr):
    queue = []
    for i in arr:
        if not queue or queue[-1] != i:
            queue.append(i)
            
    return queue