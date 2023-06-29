# https://www.codechef.com/problems/MINPIZZA

# 1 pizza = 4 slices 
import math
for i in range(int(input())):
    a, b = map(int, input().split())
    noPizza_required = math.ceil((a * b) / 4)
    print(noPizza_required)
    
    
