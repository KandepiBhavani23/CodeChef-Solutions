# https://www.codechef.com/problems/FAVOURITENUM

for _ in range(int(input())):
    num = int(input())
    if((num % 2 == 0 ) and (num % 7 == 0)):
        print("Alice")
    elif((num % 2 != 0) and (num % 9) == 0):
        print("Bob")
    else:
        print("Charlie")
        
