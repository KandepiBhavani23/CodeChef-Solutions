# https://www.codechef.com/problems/MAKEAP

for _ in range(int(input())):
    a, c = map(int, input().split())
    if(a+c)%2==0:
        print((a+c)//2)
    else:
        print(-1)
   
    
