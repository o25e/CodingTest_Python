H, M = map(int, input().split())

H = H-1
if 0 <= M <= 44:
    M = M+15
elif M == 45:
    M = 0
    H = H+1
else:
    M = M-45
    H = H+1

if H == -1:
    H = 23

print(H, M)