# https://www.codechef.com/problems/MANGOES

for _ in range(int(input())):
    mango, truck, bridge = map(int, input().split(" "))
    max_mangoes = (bridge - truck) // mango
    print(max_mangoes)
    
