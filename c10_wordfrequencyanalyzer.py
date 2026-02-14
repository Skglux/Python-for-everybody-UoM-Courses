"""  
The Task: Write a script that reads a massive text file (like a 10MB Gutenberg ebook) and returns the Top 10 most frequent words, but with these constraints:
Exclude "Stop Words": Ignore common words like the, a, an, in, or, is.
Normalization: "Python," "python!", and "PYTHON" must count as the same word.
The Goal: Learn to handle "dirty" data and optimize dictionary lookups.
"""

fhand = open("TomSawyer.txt","r", encoding="utf-8")
punctuations = ".,!?;:\"()"
stopwords = ["the","a","an","in","is"]
cleanlist = list()
x = 0
wfrequ = dict()

for lines in fhand:
    lines = lines.rstrip()
    lines = lines.lower()
    words = lines.split()
    for word in words:
        word = word.strip(punctuations)
        if word not in stopwords:
            cleanlist.append(word)
for cleanword in cleanlist:
    wfrequ[cleanword]=wfrequ.get(cleanword,0)+1

lst = list()
for key,val in list(wfrequ.items()):
    lst.append((val,key))
lst.sort(reverse=True)

for val,key in lst[:10]:
    print(key,val)


            