#D21CE161 Parth Goswami
#e. Write a Python script to concatenate following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
#creating empty dictionary to store all other dictionary items
dic4={}
#using for loop getting all values from all dictionary
for d in (dic1,dic2,dic3):
    dic4.update(d)
print("Dictionary1:",dic1)
print("Dictionary2:",dic2)
print("Dictionary3:",dic3)    
print("Dictionary4:",dic4)
