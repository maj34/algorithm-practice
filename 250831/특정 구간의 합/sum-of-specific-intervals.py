n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

def index_sum(arr, queries):
    for i in queries:
        print(sum(arr[i[0]-1:i[1]]))

index_sum(arr, queries)

