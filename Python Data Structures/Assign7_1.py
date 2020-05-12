#Write a program that prompts for a file name, then opens that file and reads
#through the file, and print the contents of the file in upper case. Use the
#file words.txt to produce the output below.
#You can download the sample data at http://www.py4e.com/code3/words.txt
#Date :- 26 April 2020
#Done By :- Vikas Dongare
fname = input("ENTER FILE NAME: ")
fn = open(fname,'r')
for line in fn:
    line = line.rstrip()
    print(line.upper())
