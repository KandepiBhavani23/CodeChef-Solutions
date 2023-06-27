# https://www.codechef.com/problems/DOREWARD

for _ in range(int(input())):
    donations = int(input())
    if(donations <= 3):
        print("BRONZE")
    elif(donations > 3 and donations <= 6):
        print("SILVER")
    else:
        print("GOLD")
