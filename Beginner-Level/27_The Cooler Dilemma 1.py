# https://www.codechef.com/problems/WATERCOOLER1

for _ in range(int(input())):
    cost_rent_cooler, purchase_cooler, months = map(int, input().split())
    rent_cooler = cost_rent_cooler * months
    if(rent_cooler < purchase_cooler):
        print("Yes")
    else:
        print("No")
    
