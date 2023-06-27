# https://www.codechef.com/problems/ONEFULPAIRS

a, b = map(int, input().split())
one_pair = (a + b) + (a * b)
if(one_pair == 111):
    print("YES")
else:
    print("NO")
