# https://www.codechef.com/problems/JASSIGNMENTS

# Total Assignments : 3
# Duration of 1 assignment = 1 hr
# Time Limit = 10 PM

for _ in range(int(input())):
    start_time = int(input())
    end_time = 10
    if(start_time + 3 <= end_time):
        print("Yes")
    else:
        print("No")
