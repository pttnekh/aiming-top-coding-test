def solution(numbers):
    strs = [str(num) for num in numbers]
    strs.sort(key=lambda x:x*3, reverse = True)
    answer = ''.join(strs)
    return str(int(answer)) if answer else '0'