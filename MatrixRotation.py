

import numpy as np

input = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
new_input = np.zeros((4,4))
n = 3
for i in range(0,3):
    for j in range(0,3):
        if(n-j>0):
            l = n-j
            row = j
        else:
            l = j
        if(row>0):
            m = i+row
        else:
            m = i
        new_input = input[l][m]

print(new_input)