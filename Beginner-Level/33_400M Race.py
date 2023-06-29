# https://www.codechef.com/problems/RACE400M

for _ in range(int(input())):
    alice, bob, charlie = map(int, input().split())
    alice_speed = 400/alice 
    bob_speed = 400/bob 
    charlie_speed = 400/charlie 
    
    if(max(alice_speed, bob_speed, charlie_speed) == alice_speed):
        print("ALICE")
    elif(max(alice_speed, bob_speed, charlie_speed) == bob_speed):
        print("BOB")
    else:
        print("CHARLIE")
    
