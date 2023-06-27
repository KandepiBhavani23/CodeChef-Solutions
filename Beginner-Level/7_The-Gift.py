# https://www.codechef.com/problems/CS2023_GIFT

total_amount, price, amount_present = map(int, input().split())

if(total_amount >= price):
    print("YES")
elif(total_amount + amount_present >= price):
    print("YES")
else:
    print("NO")
