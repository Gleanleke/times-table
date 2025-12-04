def studentMarksList(x,y):
    studentMarks=x
    
    average=0
    x=0
    for x in range(0,len(studentMarks)):
        average=average+studentMarks[x]
    average=(average/len(studentMarks))
    print(f"class of {y}")
    print(f"Class average= {average}")

    highestScore=max(studentMarks)
    print(f"Class highest score= {highestScore}")
    
    lowestScore=min(studentMarks)
    print(f"Class lowest score= {lowestScore}")

    sortedList=sorted(studentMarks)
    print(f"the sorted list in ascending order is {sortedList}")