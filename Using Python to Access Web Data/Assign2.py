#In this assignment you will read through and parse a file with text and numbers
#You will extract all the numbers in the file and compute the sum of the numbers
#Date :- 29 April 2020
#Done By :- Vikas Dongare
import re

name = input("ENTER FILENAME: ")
if len(name) < 1: name = "sample.txt"
handle = open(name)
sum = 0
for line in handle:
    num = re.findall('[0-9]+',line)
    if len(num) < 1:
        continue
    for sno in num:
        no = int(sno)
        sum = sum + no

print("SUM: ",sum)
