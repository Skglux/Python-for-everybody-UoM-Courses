"""
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.
You can download the sample data at http://www.py4e.com/code3/romeo.txt

Desired Output
['Arise', 'But', 'It', 'Juliet', 'Who', 'already', 'and', 'breaks', 'east', 'envious', 'fair', 'grief', 'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft', 'sun', 'the', 'through', 'what', 'window', 'with', 'yonder']

"""
inpfile = input("Enter file name:")
fhand = open(inpfile)
adeia_oura = []
for lines in fhand:
    oura = lines.split() 
    for word in oura:
        if not word in adeia_oura:
            adeia_oura.append(word)
adeia_oura.sort()
print(adeia_oura)
        
        
    


