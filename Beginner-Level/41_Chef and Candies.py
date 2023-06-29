# https://www.codechef.com/problems/CHEFCAND

""" 
1 packet = 4 candies

"""
import math
for _ in range(int(input())):
    children, candies = map(int, input().split())
    if(children <= candies):
        print(0) 
    else:
        print(math.ceil((children - candies)/4))
    
        
