#SECTION - LIST IN PYHTON
#LISTS ARE MUTABLE IN PYTHON, WE CAN ACCESS ANY INDEX OF LISTS AND CAN CHANGE IT

# student = ["ammaarah" , 95.5, 23]
# student[2] = 24
# print(student)

#SCLICING INDEX IN PYTHON
# Marks = [10, 20, 30, 40]
# Marks[0:2] 
# Marks[2] = 35
# print(Marks[0:2])
# print(Marks[2])

#negative indexing in python
# Marks = [10, 20, 30, 40]
# print(Marks[-2:-1])
# print(Marks[:-1])
# print(Marks[-4:-1])

#WAP to input users first name and print its length
# name = str(input("enter users first name"))
# print(len(name))

# sen = " $ % $ $"
# print(sen.count('$'))

#NOTE list methods 
# list = [1, 2, 3]
# list.append(4)
# list.sort()
# list.sort(reverse= True )
# list.reverse()
# list.insert(0, 0)
# print(list)
#NOTE - 
#tuples and almost similar to strings, 
# but the major difference is string is mutable we can add value 
# into string but tuples and immutable 

#SECTION -  - TUPLE METHODS 
# tup = [1,2,3]
# print(tup.index(1)) #it means 1 element ka index 0 hai

# tup = [1, 2,3,1,3,6]
# print(tup.count(1)) #it tells the count of elements in tuple

#TODO - WAP TO ASK USER TO ENTER NAMES of THEIR 3 FAV MOVIES & STORE THEM IN A LIST 
# movies = []
# first_fav_movie = str(input(" enter your top 1st fav movie "))
# second_fav_movie = str(input(" enter your top 2nd fav movie "))
# third_fav_movie = str(input(" enter your top 3rd fav movie "))
# movies.append(first_fav_movie)
# movies.append(second_fav_movie)
# movies.append(third_fav_movie)
# print(movies)

#NOTE - OR THE GIVEN BELOW METHOD 
# movies= []
# mov123 = str(input("enter you 3 fav movies"))
# movies.append(mov123)
# print(movies)

#NOTE - OR THE GIVEN BELOW METHOD 
# movies= []
# movies.append(str(input("enter you 1st fav movies")))
# movies.append(str(input("enter you 2nd fav movies")))
# movies.append(str(input("enter you 3rd fav movies")))
# print(movies)

#TODO - WAP TO CHECK IF A LIST CONTAINS A
#  PALINDROME OF ELEMENTS (HINT: USE COPY() METHOD)
# list1 = ["g","a","r","a","g"]
# list2 = [1,2,3]
# copy_list1 = list1.copy()
# copy_list1.reverse()

# if (copy_list1 == list1):
#     print("PALENDROME")
# else:
#     print("!palendrome")

#TODO - WAP TO COUNT THE NUMBER OF STUDENTS WITH THE "A" GRADE IN THE FOLLOWING TUPLES
# ["C", "D", "A", "A", "B", "B", "A"]

# tup = ("C", "D", "A", "A", "B", "B", "A")
# print(tup.count("A"))

#TODO - STORE THE ABOVE VALUES IN A LIST & sort them from "a" to "d"
# list = ["C", "D", "A", "A", "B", "B", "A"]
# list.sort()
# print(list)

#SECTION - SETS IN PYTHON 
# SET IS THE COLLECTION OF THE UNORDERED ITEMS, EACH ELEMENT IN THE SET MUST BE UNIQUE AND IMMUTABLE although set is mutable
# WE CANNOT STORE LIST AND DICTIONARY IN OUR SETS AS, THEY BOTH ARE MUTABLE as elements in our set ARE IMMUTABLE 
# SET DOESNT CONTAINS KEYVALUE PAIRS LIKE DICTIONARY IT ONLY CONTAINS KEYS 
# set = {1, 2, 2, 3, "hello", 89.9 , "hello"}
# print(set) # set ignores duplicates inside the set also it is unordered 
# print(len(set)) #length also ignored duplicate items 

#NOTE - empty set
# empty = set()
# print(type(empty))

#SECTION - METHODS OF SETS 
#set.add(el)              #adds an element
#set.remove(el)           #removes an element
#set.clear()              #empties the set
#set.pop()                #removes a random value 
#set.union(set2)          #combines both set values & return new
#set.intersection(set2)   #combines common values & returns new 
#set have unhashable values

# set1 = {1,2,3}
# set2 = {2,3,4}
# print(set1.union(set2)) #set.union returns its unique ans, no changs occues in set1 and set2 
# print(set1)
# print(set2)
# print(set1.intersection(set2))

#TODO - PRACTICE QUESTION
#STORE THE FOLLOWING WORD MEANINGS IN A PYTHON DICTIONARY
# dict= {
#     "table" :'a piece of furniture ' , "list of facts and figures"
#     "cat" : " a small animal"
# }
# print(dict)

# #TODO - you are given a list of subjects for students. Assume one classroom is required for 1 subject
# #how many classrooms are needed by all students 
# set = {"python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"}
# print(len(set))

#TODO - WAP TO ENTER MARKS OF 3 SUBJECTS FROM THE USER AND STORE THEM IN A DICTIONARY. START WITH AN EMPTY 
# DICTIONARY AND add one by one.use subject name as key & marks as value 
# marks = {}
# subj1 = int(input("enter the marks of subject1 "))
# subj2 = int(input("enter the marks of subject2 "))
# subj3 = int(input("enter the marks of subject3 "))
# marks.update ({"subj1" : subj1})
# marks.update ({"subj2" : subj2})
# marks.update ({"subj3" : subj3})
# print(marks)

#TODO - figure out the way to store 9 & 9.0 as seperate values in the set
# (you can take help of built in data types )
set = {9, 9.0}
print(set)
# PYHTON TREATS 9 AND 9.0 AS SAME 
# WE CAN SAVE IN STRING FORM 
set = {9 , "9.0"}
print(set)
#or we can save through builtin data types as tuples bcx tuples are immutable 
values = {
    ("float", 9.0),
    ("int" , 9)
}
print(values)
