# https://www.codechef.com/problems/CHEAPFOOD

for _ in range(int(input())):
    bill = int(input())
    first_coupon = bill * (10/100)
    second_coupon = 100 
    max_discount = int(max(first_coupon, second_coupon))
    print(max_discount)
