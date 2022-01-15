#D21CE161 Parth Goswami
#c. Write a Python program to sum all the items in a dictionary.


dictionary = {1: 500, 2:600, 3:700,4:800}
print("Dictionary:",dictionary)

#Function to print sum
def ReturnSum(MyDictionary):

    list = []
    for i in MyDictionary:
        list.append(MyDictionary[i])
    final = sum(list)
    return final
# sumation of values of dictionary
print("Sum:",ReturnSum(dictionary))