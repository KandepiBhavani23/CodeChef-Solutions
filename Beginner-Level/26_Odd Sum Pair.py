# https://www.codechef.com/problems/ODDSUMPAIR

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    odd_numbers = ((a + b) % 2 != 0 or (b + c) % 2 != 0 or (c + a) % 2 != 0)
    if(odd_numbers):
        print("Yes")
    else:
        print("No")
