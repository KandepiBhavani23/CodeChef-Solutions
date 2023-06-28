# https://www.codechef.com/problems/NETFLIX

for _ in range(int(input())):
    alice, bob, charlie, sub_cost = map(int, input().split())
    buy_sub = alice + bob >= sub_cost or bob + charlie >= sub_cost or charlie + alice >= sub_cost
    if(buy_sub):
        print("YES")
    else:
        print("NO")
