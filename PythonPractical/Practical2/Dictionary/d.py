#D21CE161 Parth Goswami
#d. Write a Python script to add a key to a dictionary.

Dictionary = {0:10,1:20}
print(Dictionary)
key=int(input("Enter key to add:"))
value=int(input("Enter value to key:"))
Dictionary.update({key:value})
print(Dictionary)