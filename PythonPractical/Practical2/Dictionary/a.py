#D21CE161 Parth Goswami
#a. Write a Python script to check whether a given key already exists in a dictionary.

#function to check key is present in dictionary
def ChKey(AlphaNumeric,ckey):
    if ckey in AlphaNumeric.keys():
        print("Present, ", end =" ")
        print("value =", AlphaNumeric[ckey])
    else:
        print("Not present")

#Dictionary
AlphaNumeric={'a':1,'b':2,'c':3,'d':4}

print(AlphaNumeric)
ckey='a'
ChKey(AlphaNumeric,ckey)
ckey='z'
ChKey(AlphaNumeric,ckey)
