def solution(array, commands):
    value = []
    for i, j, k in commands:
        value.append(sorted(array[i-1:j])[k-1])
    return value
