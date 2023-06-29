# https://www.codechef.com/problems/EXPERT

for _ in range(int(input())):
    a, b = map(int, input().split())
    problems_solved = int((b /a) * 100)
    if(problems_solved >= 50):
        print("YES")
    else:
        print("NO")
