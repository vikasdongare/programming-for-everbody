#Write a program that repeatedly prompts a user for integer numbers until the
#user enters 'done'. Once 'done' is entered, print out the largest and smallest
#of the numbers. If the user enters anything other than a valid number catch it
#with a try/except and put out an appropriate message and ignore the number.
#Enter 7, 2, bob, 10, and 4 and match the output below.
#Date :- 26 April 2020
#Done By :- Vikas Dongare

smallest = None
largest = None
while True :
    sval = input('ENTER NUMBER: ')
    if sval == "done":
        break
    try :
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = fval
    if fval < smallest:
        smallest = fval
    if largest is None:
        largest = fval
    if fval > largest:
        largest = fval
print('Maximum is',largest)
print('Minimum is',smallest)
