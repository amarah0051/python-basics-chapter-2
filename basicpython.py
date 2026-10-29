# confirming the datatype 
# name = "amarah"
# age = 24
# cgpa = 2.78
# her = False
# him = None
# print(type(name) , type(age) , type(cgpa) , type(her) , type(him))



# write a code to print sum of 2 numbers 

# a = 2 
# b = 3
# sum = a + b
# print(sum)
# print(sum([a , b]))



# TAKING INPUT AND STORING IT 
# name = input("my name is: ")
# print(name)
# name = input("name :")
# age = input()
# price = input()
# print("my name is " , name, "my age is" , age , "and the price is" , price)

#print grades of students

# marks = int(input("enter the marks"))
# if(marks >= 90):
#     print("A")
# elif(marks < 90) and (marks >= 75):
#     print("B")
# elif(marks < 75) and (marks >= 60):
#     print("C")
# elif(marks < 60):
#     print("D")
# else:
#     print("fail")

#type casting in python
# num = 3.14
# num = str(num)
# print(type(num))

#taking input in python (syntax)
# name= input("enter your name")
# print("welcome", name)
# age = input("enter your age")
# print("i am" , age , "years old")

#result of input always appears in string in the terminal,
#for float or int we have to define the datatype by type casting
# value = input("enter your age")
# print(type(value))

# price = float(input("enter the price"))
# print(type(price), price)

#write a program to enter input of 2 numbers
# num1 = float(input("enter first number"))
# num2 = int(input("enter second number"))
# sum = num1 + num2 
# print("the sum is ", sum)

#WAP to input side of a square and print its area
# side_square = int(input("enter side of a square"))
# area = side_square * side_square    # side_square * * 
# print("the area is ", area)

# #WAP to input side of square and print its perimeter 
# side_square = int(input("enter side of a square"))
# perimeter = 4 * side_square
# print("the perimter of square is", perimeter)


#WAP to input floating point numbers and print their avg

# num1 = float(input("enter fisrt num"))
# num2 = float(input("enter second num"))
# avg = ((num1 + num2) / 2) # putting (num1+num2) so that later it can divide by total
# print("the avg is ", avg)

# num1 = float(input("enter fisrt num"))
# num2 = float(input("enter second num"))
# total_count = len([num1 , num2])
# avg = ((num1 + num2) / total_count) # putting (num1+num2) so that later it can divide by total
# print("the avg is ", avg)

#WAP TO INPUT 2 INT NUMBERS, A & B PRINT TRUE IF A IS GREATER THEN OR EQUAL TO B . IF NOT PRINT FALSE

A = int(input('enter first number'))
B = int(input(' enter 2nd number'))
if(A>=B):
    print("true")
else:
    print("false")
