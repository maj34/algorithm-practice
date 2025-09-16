string = input()

cnt_ee = 0
cnt_eb = 0

for i in range(len(string)-1):
    if 'ee' == string[i:i+2]:
        cnt_ee += 1
    elif 'eb' == string[i:i+2]:
        cnt_eb += 1

print(cnt_ee, cnt_eb)