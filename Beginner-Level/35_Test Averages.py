# https://www.codechef.com/problems/TESTAVG

for _ in range(int(input())):
    score1, score2, score3 = map(int, input().split())
    first_two = (score1 + score2)/2 < 35
    second_last = (score2 + score3)/2 < 35
    last_first = (score3 + score1)/2  < 35 
    if(first_two or second_last or last_first):
        print("Fail")
    else:
        print("Pass")
    
