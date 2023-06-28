# https://www.codechef.com/problems/DOMINANT

for _ in range(int(input())):
    army1, army2, army3 = map(int, input().split())
    dominant = army3 > army1 + army2 or army1 > army2 + army3 or army2 > army3 + army1
    if(dominant):
        print("YES")
    else:
        print("NO")
