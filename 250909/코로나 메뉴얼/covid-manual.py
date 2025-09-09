As, At = input().split()
Bs, Bt = input().split()
Cs, Ct = input().split()

def symptom(s, t):
    if s == "Y" and int(t)>=37:
        return "A"
    elif s == "N" and int(t)>=37:
        return "B"
    elif s == "Y" and int(t)<37:
        return "C"
    else:
        return "D"

if symptom(As, At)=="A" and symptom(Bs, Bt)=="A":
    print("E")
elif symptom(As, At)=="A" and symptom(Cs, Ct)=="A":
    print("E")
elif symptom(Bs, Bt)=="A" and symptom(Cs, Ct)=="A":
    print("E")
else:
    print("N")