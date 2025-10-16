arr = list(map(int, input().split()))

# Please write your code here.
import itertools

def min_capability_difference(devs):
    min_diff = float('inf')
    found = False
    
    # 첫 번째 팀(2명)을 고르는 조합
    for team1 in itertools.combinations(range(5), 2):
        remaining1 = [i for i in range(5) if i not in team1]
        # 두 번째 팀(2명)을 고르는 조합
        for team2 in itertools.combinations(remaining1, 2):
            remaining2 = [i for i in remaining1 if i not in team2]
            team3 = remaining2  # 마지막 한 명
            
            # 팀 능력치 합 계산
            t1_sum = sum(devs[i] for i in team1)
            t2_sum = sum(devs[i] for i in team2)
            t3_sum = sum(devs[i] for i in team3)
            
            # 모두 달라야 함
            if len({t1_sum, t2_sum, t3_sum}) == 3:
                diff = max(t1_sum, t2_sum, t3_sum) - min(t1_sum, t2_sum, t3_sum)
                min_diff = min(min_diff, diff)
                found = True

    return min_diff if found else -1


print(min_capability_difference(arr))