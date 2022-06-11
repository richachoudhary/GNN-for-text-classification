import re


CNT = 10

i = 0

with open('data\mr_new.txt' , 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if i > CNT: 
            break
        i += 1
        tmp = line.split("\t")
        print(tmp)