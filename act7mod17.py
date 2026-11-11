scores=[85, 90, 75, 95, 80, 88, 70]

input("list:"+str(scores)+" n=9 press enter")
guess=input("max check to find any number in this list?")
target=int(input("pick a number from the list:"))

input("binary search-checks the meiddle,drops half each round.press enter")
low,high=0,len(scores)-1
steps=0
while low<=high:
    mid = (low+high)//2
    steps+=1
    print("round",steps,"-> checked",scores[mid])
    if scores[mid]==target:
        print("Number found at index:", mid)
        break
    else:
       print("Number not found")
    high=mid-1
print("found",target,"at position",mid+1,"in",steps,"steps your guess:",guess,"-> 0(log n)")