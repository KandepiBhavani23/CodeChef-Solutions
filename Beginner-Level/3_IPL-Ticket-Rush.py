# https://www.codechef.com/problems/IPLTRSH

for _ in range(int(input())):
    students, tickets = map(int, input().split())
    tickets_available = students - tickets 
    if(tickets_available <= 0): 
        print(0)
    else:
        print(tickets_available)
