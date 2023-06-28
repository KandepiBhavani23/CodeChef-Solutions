# https://www.codechef.com/problems/F1RULE

for _ in range(int(input())):
    fastest_finish_time, chef_time = map(int, input().split())
    if((fastest_finish_time * 1.07) >= chef_time):
        print("YES")
    else:
        print("NO")
