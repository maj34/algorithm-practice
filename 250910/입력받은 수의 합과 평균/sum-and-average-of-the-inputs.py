N = int(input())

val_sum = 0
for _ in range(N):
    a = int(input())
    val_sum+=a

print(f"{val_sum} {val_sum/N:.1f}")