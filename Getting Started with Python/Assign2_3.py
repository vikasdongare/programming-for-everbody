#Write a program to prompt the user for hours and rate per hour using input to
#compute gross pay. Use 35 hours and a rate of 2.75 per hour to test the program
#(the pay should be 96.25). You should use input to read a string and float()
#to convert the string to a number. Do not worry about error checking or bad
#user data.
#Date :- 24 april 2020
#Done by :- Vikas Dongare

hours = input('ENTER HOURS : ')
rate = input('ENTER RATE PER HOUR :')
hours = float(hours)
rate = float(rate)
pay = hours * rate
print('PAY :',pay)
