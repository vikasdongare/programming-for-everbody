#Write a program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages. You can pull the
#hour out from the 'From ' line by finding the time and then splitting the
#string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.
#Date :- 28 April 2020
#Done By :- Vikas Dongare
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time = dict()

for line in handle:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    pos = line.find(':')
    try:
        hour = int(line[pos-2:pos])
    except:
        continue
    #print(hour)
    time[hour] = time.get(hour,0) + 1

lst = list()
for k,v in time.items():
    newtup = (k,v)
    lst.append(newtup)

lst = sorted(lst,reverse=False)
for k,v in lst:
    print(k,v)
