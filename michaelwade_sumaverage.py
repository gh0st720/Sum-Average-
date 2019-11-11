#Sum/Average Program
#Your first and last name: Michael Wade
#Your student ID: s1296926

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers (integers)
#Instead of searching for a name in the list
#   Compute the sum of all 20 numbers
#   Compute the average for all 20 numbers

#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:

#List creation

n = input("Enter Number to calculate sum")

n = int (n)
average = 0
sum = 0
for num in range(0, n+1, 1):
    sum = sum+num
print("SUM of first ", n, "numbers is: ", sum )

print ("calculate an average of first n natural numbers")

n = input("Enter Number ")
n = int (n)
average = 0
sum = 0
for num in range(0,n+1,1):
    sum = sum+num;
average = sum / n
print("Average of first ", n, "number is: ", average)
