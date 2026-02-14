"""  
Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
Desired Output
04 3
06 1
07 1
09 2
10 3
11 6
14 1
15 2
16 4
17 2
18 1
19 1

"""

finp=input("Enter a file name:")
fhand = open(finp)
hours = dict()
for lines in fhand:
    lines = lines.rstrip()
    if lines.startswith("From") and lines.endswith("2008"):
        words = lines.split()
        twodigit = words[5][0:2]
        hours[twodigit]=hours.get(twodigit,0)+1
t = list(hours.items())
t.sort()
for k,v in t:
    print(k,v)



        