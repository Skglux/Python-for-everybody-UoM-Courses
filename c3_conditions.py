score = input("Enter score with a range from 0.0 to 1.0 ")
fscore = float(score)

if fscore < 0.0 or fscore > 1.0 :
    print("Error score is out of range")
    quit()
    
if fscore < 0.6:
    print("F")

elif fscore < 0.7:
    print("D")
    
elif fscore < 0.8:
    print("C")
    
elif fscore < 0.9:
    print("B")

else :
    print("A")