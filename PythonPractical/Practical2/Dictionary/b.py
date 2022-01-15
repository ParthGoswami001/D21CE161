#D21CE161 Parth Goswami
#b. Write a Python script to merge two Python dictionaries.

#Dictionary 1
Dictionary1={1:'apple',2:'banana',3:'cherry'}
#Dictionary 2
Dictionary2={4:'dates',5:'orange'}
#Dictionary 3 in which Dictionary1 and Dictionary2 merge
Dictionary3=Dictionary1.copy()
Dictionary3.update(Dictionary2)
#printing all dictionary
print("Dictionary1:",Dictionary1)
print("Dictionary2:",Dictionary2)
print("Dictionary3:",Dictionary3)
