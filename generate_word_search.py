import math
import random
import csv
from os import path as path_lib

s = 100
SIZE = range(s)

def calc_p(x,y):
    #normalise to 0-1
    p = -1
    while (p == -1): 
        _x = x/s 
        _y = y/s
        domain = (s*s-1)/(s*s)
        log_internal = (1/domain)-1
        x_incep = math.log(log_internal)
        v = _x*_y+_x+x_incep
        p = 1/(1+math.e**-v)
    return p  
    
def generate():
    semi_colon_placed = False
    while (semi_colon_placed == False):
        word_search = []
        for x in SIZE:
            row = []
            for y in SIZE:
                char = ':'
                if random.random() < calc_p(x,y) and not semi_colon_placed:
                    char = ';'
                    semi_colon_placed = True
                row.append(char)
            word_search.append(row)
    return word_search

def print_wordsearch(ws):
    for x in SIZE:
        print('')
        for y in SIZE:
            print(ws[x][y],end=' ')




ws = generate()
semi = ''.join(str(item) for innerlist in ws for item in innerlist).find(';')
print_wordsearch(ws)




with open(path_lib.join(path_lib.abspath(__file__),'..\\wordsearch.csv'),"w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(ws)