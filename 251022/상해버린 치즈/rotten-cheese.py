N, M, D, S = map(int, input().split())

p, m, t = [], [], []
for _ in range(D):
    person, milk, time = map(int, input().split())
    p.append(person)
    m.append(milk)
    t.append(time)

sick_p, sick_t = [], []
for _ in range(S):
    person, time = map(int, input().split())
    sick_p.append(person)
    sick_t.append(time)

eats = [[101] * (M + 1) for _ in range(N + 1)]

# D개의 기록을 순회하며 가장 빨리 먹은 시간으로 업데이트
for i in range(D):
    person = p[i]
    cheese = m[i]
    time = t[i]
    eats[person][cheese] = min(eats[person][cheese], time)

suspect_cheeses = []

# 1번 치즈부터 M번 치즈까지 하나씩 확인
for cheese_id in range(1, M + 1):
    is_suspect = True  # 이 치즈가 상했다고 가정
    
    # 모든 아픈 사람을 확인
    for i in range(S):
        person = sick_p[i]
        sick_time = sick_t[i]
        
        # 이 아픈 사람이 이 치즈를 먹은 시간
        eat_time = eats[person][cheese_id]
        
        # 만약 먹은 적이 없거나 아프거나 아픈 이후에 먹었다면
        if eat_time >= sick_time:
            is_suspect = False # 이 치즈는 상한 치즈가 아님
            break # 다음 치즈로 넘어감
    
    # 모든 아픈 사람이 아프기 전에 이 치즈를 먹었다면
    if is_suspect:
        suspect_cheeses.append(cheese_id)

# 약이 필요한 사람을 기록
people_need_medicine = set()

# D개의 모든 먹은 기록을 다시 확인
for i in range(D):
    person = p[i]
    cheese = m[i]
    
    # 이 사람이 먹은 치즈가 용의선상에 있다면
    if cheese in suspect_cheeses:
        # 약이 필요한 사람 목록에 추가
        people_need_medicine.add(person)

print(len(people_need_medicine))