# https://www.codechef.com/problems/SUBSCRIBE_

import math
for _ in range(int(input())):
    persons, amount = map(int, input().split())
    total_sub = math.ceil(persons / 6)
    total_cost = total_sub * amount
    print(total_cost)
 
