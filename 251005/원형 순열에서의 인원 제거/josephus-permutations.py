from collections import deque
import sys

N, K = map(int, input().split())

dq = deque(range(1, N+1))
order = []

while dq:
    dq.rotate(-(K-1))   # K번째가 맨 앞에 오도록 왼쪽으로 회전
    order.append(dq.popleft())

print(*order)