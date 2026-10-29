#strings in python are written by '' , "" , ''' '''
#adding 2 strings together is contatenation 

# str1 = "hello"
# len1 = len(str1)
# print(len1)

# str2 = "world"
# len2 = len(str2)
# print(len2)

# print(str1 + " " + str2)

# final_str = len1 + len2
# print(final_str)

#indexing 
# str = "hello world"
# character = str[0] , str[1] , str[2] , str[3] , str[4] , str[5] , str[6] , str[7] , str[8] , str[9] , str[10]
# print(character)

# #slicing 
# str = "i am ammarah"
# print(str[1:6])
# print(str[0:len(str)]) #len(str) = last index 
# print(str[0:]) #if we donot write last index i will auto goes till last
# print(str[:13]) #it auto detech 1st index

#negative index

# str = "apple"
# print(str[-3:-1])

#----PRACTICE QUESTION----
#WAP to input user's first name & print its length
# f_name = input()
# print(len(f_name))

#WAP to find occurance of "$" in a string
# str= "hi $$$$$$"
# print(str.count("$"))

#-------CONDITIONAL STATEMENET--------
# if age >=18 allow to vote
# age = int(input("enter your age"))
# if(age >= 18):
#     print("yes, you can vote")
# elif(age <= 18):
#     print("no you cannot")
# else:
#     print("invalid")

#-----grading system in python
# marks = int(input("enter your marks"))
# if(marks >= 90):
#     print('A')
# elif(marks <= 90 and marks >= 80):
#     print("B")
# elif(marks <= 80 and marks >=70):
#     print("C")
# elif(marks<=70):
#     print("D")

#----nesting in python
#WAP to check if a number entered by the user is even or odd
# num = int(input("enter a number"))
# if(num%2==0):
#     print("even")
# elif(num%2==1):
#     print("odd")

#WAP to find the greatest of 3 numbers entered by user
# num1=int(input("enter 1st number"))
# num2=int(input("enter 2nd number"))
# num3=int(input("enter 3rd number"))
# if(num1>=num2 and num1>=3):
#     print(num1)
# elif(num2>=num3 and num2>=num1):
#     print(num2)
# elif(num3>=num1 and num3>=num2):
#     print(num3)
# else:
#     print("invalid")

#WAP to find the greatest of 4 numbers entered by user
# num1=int(input("enter 1st number: "))
# num2=int(input("enter 2nd number: "))
# num3=int(input("enter 3rd number: "))
# num4=int(input("enter 4rth number: "))
# if(num1>=num2 and num1>=3 and num1>=4):
#     print(num1)
# elif(num2>=num3 and num2>=num1 and num2>=num4):
#     print(num2)
# elif(num3>=num1 and num3>=num2 and num2>=num4):
#     print(num3)
# elif(num4>=num1 and num4>=num2 and num4>=num4):
#     print(num4)
# else:
#     print("invalid")


#WAP to check if a number is a multiple of 7 or not
num = int(input("enter a number"))
if(num%7 == 0):
    print("TRUE")
else:
    print("FALSE")