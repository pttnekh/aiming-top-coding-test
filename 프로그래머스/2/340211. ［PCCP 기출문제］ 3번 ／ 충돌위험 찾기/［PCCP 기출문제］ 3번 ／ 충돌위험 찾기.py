from collections import defaultdict, Counter

def solution(points, routes):
    time_pos = defaultdict(list)  # t -> [(r,c), (r,c), ...] / key: t, value: list

    for route in routes:
        t = 0
        r, c = points[route[0]-1]
        time_pos[t].append((r, c))  # 0초 시작점도 체크

        for i in range(1, len(route)):
            tr, tc = points[route[i]-1]

            while r != tr:          # r 먼저
                r += 1 if r < tr else -1
                t += 1
                time_pos[t].append((r, c))

            while c != tc:
                c += 1 if c < tc else -1
                t += 1
                time_pos[t].append((r, c))

    answer = 0
    for t in time_pos:
        cnt = Counter(time_pos[t])
        answer += sum(1 for k in cnt if cnt[k] >= 2)  # 좌표별 1회 카운트
    return answer