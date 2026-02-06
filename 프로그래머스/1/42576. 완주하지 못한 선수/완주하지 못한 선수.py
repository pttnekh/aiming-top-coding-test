from collections import Counter

def solution(participant, completion):
    count = Counter(participant)
    count.subtract(completion)
    for name in participant:
        if count[name] > 0:
            return name