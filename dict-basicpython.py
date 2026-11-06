#SECTION - DICTIONARY INPYTHON 
#KEY = VALUE , every key store some value in it, they are unordered , 
# mutable and dont allow duplicate keys 

# dict = {
#     "name" : "amarah",
#     "age " : 23,
#     "marks " : 89.9,
#     "is_adult" : True,
#     "subject" : ["python", "C", "C++" , "JAVA"],
#     "topics" : ("dict", "sets", "tuples"),
#     23 : 45.5,
#     45.5 : 45,
# }

# dict["name"] = "ahmed",
# dict["new student"] = "ayesha",
# print(dict)

# null_dict = {}
# null_dict["add key"] = "assign value"
# print(null_dict)

#SECTION - NESTED DICTIONARY
student = {
    "name" : "ammarah",
    "subject" :{
        "phy" : 97,
        "chem" : 87,
        "eng" : 90,
    }
}
# print(student)
# print(student["subject"]["chem"])

#SECTION - METHODS IN DICTIONARY
# mydict.key()                            returns all keys 
# mydict.values()                         returns all values 
# mydict.items                            returns all (key,val) pairs as tuples 
# mydict.get("key")                       returns the key according to the value 
# mydict.update(newdict)                  insert the specified item to the dict 

# print(student.keys())
# print(student.values())
# print(student.items())
#we can store list into dict and dict into list 
# print(len(list(student.keys()))) #length of list of dict's key

# 2 methods to return the value of key 
# print(student["subject"])
# print(student.get("subject")) #best approach
# student.update({"name" : "ayesha"})
# print(student)

#if we want to store new dict and to update it 
new_dict = {"city" : "ryk"}
student.update(new_dict)
print(student)