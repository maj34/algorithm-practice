skills = list(map(int, input().split()))

# 정렬
skills.sort()

# 팀 구성: (가장 작은 + 가장 큰), (두 번째 작은 + 두 번째 큰), (세 번째 작은 + 세 번째 큰)
team1 = skills[0] + skills[5]
team2 = skills[1] + skills[4]
team3 = skills[2] + skills[3]

# 팀별 합 저장
teams = [team1, team2, team3]

# 최대 팀 - 최소 팀
result = max(teams) - min(teams)
print(result)