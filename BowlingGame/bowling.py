from framescore.py import frame_score
from framescore.py import read_ragged_array
fin = input("Input filename: ", "r")
read_ragged_array(fin)
frames = read_ragged_array

score = 0
For i in range (1, 11):
    if frames[i][0] == 10 and frames [i+1][0] == 10:
    bonus1 += 10
    frames[i+2][0] == bonus2
    elif frames[i][0] == 10 and frames [i+1][0] < 10:
    bonus1 += frames[i+1][0]
    bonus2 += frames[i+1][1]
    elif (frames[i][0] + frames[i][1]) ==10:
    bonus1 += frames[i+1][0]
    bonus2 == 0
    else:
    bonus1 == 0
    bonus2 == 0
    score += framescore(frames[i], bonus1, bonus2)
print(score)
    
    











