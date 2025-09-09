Am, Ae = map(int, input().split())
Bm, Be = map(int, input().split())

if Am > Bm:
    print("A")
elif Bm > Am:
    print("B")
elif Am == Bm and Ae > Be:
    print("A")
else:
    print("B")