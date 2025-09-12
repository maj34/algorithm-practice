N = int(input())
arr = map(float, input().split())

mean_val=sum(arr)/N
print(f"{mean_val:.1f}")

if mean_val >= 4.0:
    print("Perfect")
elif mean_val >= 3.0:
    print("Good")
else:
    print("Poor")