# https://www.codechef.com/problems/WATERFILLING

for _ in range(int(input())):
    b1, b2, b3 = map(int, input().split())
    if b1==0 and b2==0 and b3==0:
        print("Water filling time")
    elif (b1==0 and b2==0) or (b2==0 and b3==0) or (b3==0 and b1==0):
        print("Water filling time")
    else:
         print("Not now")
