# https://www.codechef.com/problems/SUGARCANE

""" 
1 glass juice = 50 coins
20% of total income = sugarcane
20% of total income = salt and mint leaves
30% of total income = rent
"""

for _ in range(int(input())):
    juice = int(input())
    total_coins = juice * 50 
    sugar_salt_mint = 2 * (0.20 * total_coins)
    rent = 0.30 * total_coins
    
    profit = (total_coins - (sugar_salt_mint + rent))
    print(int(profit))
    
