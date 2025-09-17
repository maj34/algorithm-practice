char = input()

val_sum = 0
for i in char:
    if 48 <= ord(i) <= 57:
        val_sum+=int(i)

print(val_sum)