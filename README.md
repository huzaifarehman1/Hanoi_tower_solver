# Hanoi_tower_solver

## input:
n (number of towers) -> number of towers in the puzzle


c (capacity) -> number of rings each tower can hold


m (number of rings) -> number of rings in the puzzle must be <= c*n

c must be >=m for it to work

DEFAULT:
    m = 3
    c = 3 
    n = 3
## Note
for this version i dont allow user to mess c but new version will be uploaded with c as a variable 

in this version c=m
## solver logic

it uses A* to solve the puzzle by continuesly storing its child and visiting best child 

the heuristic Function or the evaluation of state is based on following

1: 

for more see rules.txt 