# https://www.codechef.com/problems/CHEFCHOCO

for _  in range(int(input())):
    total_chocolates, chocolates_present, cost_each_chocolate = map(int, input().split())
    buy_chocolates = (total_chocolates - chocolates_present) * cost_each_chocolate
    print(buy_chocolates)
    
