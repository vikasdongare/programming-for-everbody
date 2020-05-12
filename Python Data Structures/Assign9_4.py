#Write a program to read through the mbox-short.txt and figure out who has sent
#the greatest number of mail messages. The program looks for 'From ' lines and
#takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to
#a count of the number of times they appear in the file. After the dictionary is
#produced, the program reads through the dictionary using a maximum loop to find
#the most prolific committer.
#Date :- 27 April 2020
#Done by :- Vikas Dongare
fn = open("mbox-short.txt",'r')
count = dict()
for line in fn:
    line = line.rstrip()
    ln = line.split()
    if len(ln)<1 or ln[0] != 'From':
        continue
    count[ln[1]] = count.get(ln[1],0) + 1

bigcount = None
bigname = None
for name,cnt in count.items():
    if bigcount is None or cnt > bigcount:
        bigcount = cnt
        bigname = name
print(bigname,bigcount)
