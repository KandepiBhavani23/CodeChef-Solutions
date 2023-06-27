# https://www.codechef.com/problems/RIGHTTHERE

for _ in range(int(input())):
    total_people, capacity = map(int, input().split())
    if(total_people <= capacity):
        print("YES")
    else:
        print("NO")
