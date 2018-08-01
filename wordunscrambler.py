import re
import time
import random
import itertools
import math

finalList = []

f = open("words.txt", "r")
contents = f.read()
contentsArray = contents.split()
lens = len(contentsArray)
print(lens)
scrambledword = input('Input: ')

stuff = list(itertools.permutations(scrambledword))

inputLen = len(scrambledword)

for z in range(0, lens):
    cLense = len(contentsArray[z])
    if( cLense == inputLen):
        finalList.append(contentsArray[z])

inputLen = math.factorial(inputLen)
start_time = time.time()
for x in range(0, inputLen):
    inputstring = ''.join(stuff[x])
    for y in range( 0, lens):
        if(inputstring == finalList[y]):
            print(finalList[y])
            print("--- %s seconds ---" % (time.time() - start_time))
            quit()