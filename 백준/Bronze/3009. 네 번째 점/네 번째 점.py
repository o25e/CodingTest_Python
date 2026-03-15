x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# if (abs(x1 -x2) == 0) and (abs(y3 - y1) == 0):
#     x4 = x3
#     y4 = y2
# elif (abs(x1 - x2) == 0) and (abs(y3 - y2) == 0):
#     x4 = x3
#     y4 = y1
# elif (abs(x1 - x3) == 0) and (abs(y2 - y1) == 0):
#     x4 = x2
#     y4 = y3
# elif (abs(x1 - x3) == 0) and (abs(y2 - y3) == 0):
#     x4 = x2
#     y4 = y1
# elif (abs(x2 - x3) == 0) and (abs(y1 - y2) == 0):
#     x4 = x1
#     y4 = y3
# elif (abs(x2 - x3) == 0) and (abs(y1 - y3) == 0):
#     x4 = x1
#     y4 = y2

x4 = x1 ^ x2 ^ x3 #XOR 연산(같은 값 두 번 나오면 0이 되고, 남은 값만 남음)
y4 = y1 ^ y2 ^ y3

print(x4, y4)
