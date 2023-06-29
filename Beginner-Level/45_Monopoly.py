# https://www.codechef.com/problems/MONOPOLY2

"""
total companies = 4
if (profit made by a > sum(b + C + d)) then "Yes else "No"
"""

for _ in range(int(input())):
    l = list(map(int, input().split()))
    l.sort()
    largest = l.pop()
    if(largest > sum(l)):
        print("Yes")
    else:
        print("No")
