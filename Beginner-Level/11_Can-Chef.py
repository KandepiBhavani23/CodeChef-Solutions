# https://www.codechef.com/problems/CANCHEF

for _ in range(int(input())):
    petrol, distance = map(int, input().split())
    total_distance = 2 * distance
    total_petrol = 15 * petrol
    if(total_petrol >= total_distance):
        print("YES")
    else:
        print("NO")
