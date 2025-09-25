import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
dq = deque()
ans = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'push_front':
        dq.appendleft(int(cmd[1]))
    elif cmd[0] == 'push_back':
        dq.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        ans.append(str(dq.popleft()) if dq else '-1')
    elif cmd[0] == 'pop_back':
        ans.append(str(dq.pop()) if dq else '-1')
    elif cmd[0] == 'size':
        ans.append(str(len(dq)))
    elif cmd[0] == 'empty':
        ans.append('1' if not dq else '0')
    elif cmd[0] == 'front':
        ans.append(str(dq[0]) if dq else '-1')
    elif cmd[0] == 'back':
        ans.append(str(dq[-1]) if dq else '-1')

print('\n'.join(ans))