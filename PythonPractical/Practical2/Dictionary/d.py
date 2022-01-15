#D21CE161 Parth Goswami
#d. Write a Python script to add a key to a dictionary.

#dictionary
Dictionary = {0:10,1:20}
print(Dictionary)
#getting key and value
key=int(input("Enter key to add:"))
value=int(input("Enter value to key:"))
#using update fuction adding key and value
Dictionary.update({key:value})
print(Dictionary)