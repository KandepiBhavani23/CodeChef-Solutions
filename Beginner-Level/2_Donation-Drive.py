# https://www.codechef.com/problems/DONDRIVE

for _ in range(int(input())):
    donations, collected = map(int, input().split())
    required_donations = donations - collected
    print(required_donations)
