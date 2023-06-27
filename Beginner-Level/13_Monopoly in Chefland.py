# https://www.codechef.com/problems/MONOPOLY

for _ in range(int(input())):
    r1, r2, r3 = map(int, input().split())
    if((r1 + r2) < r3 or (r2 + r3) < r1 or (r3 + r1) < r2):
        print("Yes")
    else:
        print("No")
