import re
stu_details = {"Ramesh" : 95 ,"Suresh" : 98 , "Manish" : 94 , "Kamlesh" : 99,}
name = input("Enter the student's name: ")
key = re.findall(name,str(stu_details))
if key :
    print(f"{name}'s mark: {stu_details[key[0]]}")
else:
    print("Student not found")