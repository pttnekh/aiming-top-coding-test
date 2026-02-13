def solution(array, commands):
    answer = []
    for i, j, k in commands:
        sliced_array = sorted(array[i-1:j])
        answer.append(sliced_array[k-1])
        
    return answer