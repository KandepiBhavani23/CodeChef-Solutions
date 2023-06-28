# https://www.codechef.com/problems/CRICMATCH

for _ in range(int(input())):
    no_runs, remaining_overs = map(int, input().split())
    #1 over = 36 runs
    if(remaining_overs * 36 >= no_runs):
        print("Yes")
    else:
        print("No")
