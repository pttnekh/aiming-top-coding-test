def solution(sizes):
    longs = [max(w,h) for w,h in sizes]
    shorts = [min(w,h) for w,h in sizes]
    return max(longs) * max(shorts)