# https://www.codechef.com/problems/SEVENRINGS

""" 
valid phone number with 5 digits = 98765,10000, and 71023
invalid phone number with 5 digits(with no leading zeros) = 04123,9231, and 872310
"""

for _ in range(int(input())):
    items, cost = map(int, input().split())
    total_bill = items * cost 
    if (9999<total_bill<100000):
        print("Yes")
    else:
        print("No")
    
