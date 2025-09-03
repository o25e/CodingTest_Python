H, M = map(int, input().split())
T = int(input())

M = M+T
P = M // 60
if M < 60:
    print(H, M)
elif M >= 60:
    if H+P > 23:
        H = H+P-24
    else:
        H = H+P
    print(H, M-60*P)