# https://www.codechef.com/problems/PARLIAMENT

for _ in range(int(input())):
    member_present, voted_members = map(int, input().split())
    if (voted_members >= member_present / 2):
        print("YES")
    else:
        print("NO")
    
