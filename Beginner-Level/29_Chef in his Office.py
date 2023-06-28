# https://www.codechef.com/problems/OFFICE

# monday - thursday : X hours
# friday : Y (Y < X)

for _ in range(int(input())):
    X, Y = map(int, input().split())
    total_hours = X * 4 + Y  
    print(total_hours)
