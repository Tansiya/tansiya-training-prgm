"""The robot moves in a plane from original point(0,0),can move from up,down,left,right with ahgiven steps print.the nearest integer"""

#import for all math operation
import math
pos = [0,0]
#assing a while loop
while True:
    s = input()
#assign a if loop
    if not s:
        break;
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass
#print the nearest integer

print (int(round(math.sqrt(pos[1]**2+pos[0]**2))))
