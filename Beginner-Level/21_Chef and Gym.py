# https://www.codechef.com/problems/CGYM

for _ in range(int(input())):
    gym_membership , personal_trainer, total_budget = map(int, input().split())
    if(gym_membership + personal_trainer <= total_budget):
        print(2)
    elif( gym_membership <= total_budget):
        print(1)
    else:
        print(0)
