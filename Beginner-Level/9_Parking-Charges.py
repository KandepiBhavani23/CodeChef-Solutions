# https://www.codechef.com/problems/PARKINGCHARG

first_hour_pay , extra_hour_pay, parking_hours = map(int, input().split())

total_amount = first_hour_pay + (parking_hours - 1) * extra_hour_pay 
print(total_amount)
