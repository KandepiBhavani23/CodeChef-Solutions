# https://www.codechef.com/problems/WATERFLOW

for _ in range(int(input())):
    initial_water, max_capacity, additional_water, flow_time = map(int, input().split())
    flow_rate = initial_water + (additional_water * flow_time)
    if(flow_rate > max_capacity):
        print("OverFlow")
    elif(flow_rate == max_capacity):
        print("Filled")
    else:
        print("Unfilled")
    
    
