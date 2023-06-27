# https://www.codechef.com/problems/LEARNSQL

rows, col, extra_row = map(int, input().split())
total_cells = ( rows + extra_row ) * col 
print(total_cells)
