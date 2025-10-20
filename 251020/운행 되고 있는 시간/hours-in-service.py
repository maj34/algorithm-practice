N = int(input().strip())
times = [tuple(map(int, input().split())) for _ in range(N)]

# 운행되는 시간 계산 함수
def total_time(intervals):
    if not intervals:
        return 0
    intervals.sort()  # 시작 시간 기준 정렬
    total = 0
    start, end = intervals[0]

    for s, e in intervals[1:]:
        if s <= end:  # 겹치는 경우
            end = max(end, e)
        else:  # 겹치지 않으면 길이 더하고 새로운 구간 시작
            total += end - start
            start, end = s, e
    total += end - start
    return total

# 각 개발자를 한 명씩 제외하고 최대 운행 시간 찾기
max_time = 0
for i in range(N):
    remain = times[:i] + times[i+1:]  # i번째 제외
    max_time = max(max_time, total_time(remain))

print(max_time)