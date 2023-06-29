# https://www.codechef.com/problems/HELIUM3

for _ in range(int(input())):
    units, power, helium, helium_power = map(int, input().split())
    total_power = units * power
    funded_amount = helium * helium_power 
    
    if(funded_amount >= total_power):
        print("Yes")
    else:
        print("NO")
