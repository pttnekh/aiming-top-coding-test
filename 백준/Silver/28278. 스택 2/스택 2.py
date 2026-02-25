import sys

input = sys.stdin.readline
N = int(input())
stack = []

for i in range(N):
    cmd = list(map(int, input().split()))
    
    if cmd[0] == 1:
        stack.append(cmd[1])
    elif cmd[0] == 2:
        print(stack.pop() if stack else -1)
    elif cmd[0] == 3:
        print(len(stack))
    elif cmd[0] == 4:
        print(0 if stack else 1)
    elif cmd[0] == 5:
        print(stack[-1]if stack else -1)