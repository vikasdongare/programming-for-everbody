#Write a program that prompts for a file name, then opens that file and reads
#through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines
#and compute the average of those values and produce an output as shown below.
#Do not use the sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
#when you are testing below enter mbox-short.txt as the file name.
#Date :- 26 April 2020
#Done by :- Vikas Dongare
#Output :- Average spam confidence: 0.750718518519
fname = input("ENTER FILENAME: ")
fhandle = open(fname,'r')
count = 0
total = 0
for line in fhandle:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count = count + 1
        pos = line.find(':')
        value = float(line[pos+1:])
        total = total + value
print('Average spam confidence: ',total/count)
