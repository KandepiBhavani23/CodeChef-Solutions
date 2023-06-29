# https://www.codechef.com/problems/NOTEBOOK

"""
1kg pulp = 1000 pages 
1 notebook  = 100 pages 
10 notebook = 1000 pages

1kg pulp = 10 notebooks
"""

for _ in range(int(input())):
    pulp = int(input())
    notebooks = pulp * 10
    print(notebooks)
