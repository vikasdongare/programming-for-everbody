#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is
#out of range, print an error. If the score is between 0.0 and 1.0, print a
#grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and
#exit. For the test, enter a score of 0.85.
#Date :- 25 April 2020
#Done By :- Vikas Dongare

sscore = input("ENTER SCORE : ")
try:
    score = float(sscore)
except:
    print("\t!!! ENTER VALID INPUT !!!")
    quit()

if score>=0.0 :
    if score <= 1:
        if score >= 0.9:
            print("GRADE : A")
        elif score >= 0.8:
            print("GRADE : B")
        elif score >= 0.7:
            print("GRADE : C")
        elif score >= 0.6:
            print("GRADE : D")
        else:
            print("GRADE : F")
    else:
        print("\t!!! OUT OF RANGE INPUT !!!")
else:
    print("\t!!! OUT OF RANGE INPUT !!!")
