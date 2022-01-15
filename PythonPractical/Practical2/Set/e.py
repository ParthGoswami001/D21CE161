#D21CE161 Parth Goswami
#e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.

def most_frequent(List):
	counter = 0
	num = List[0]
	
	for i in List:
		curr_frequency = List.count(i)
		if(curr_frequency> counter):
			counter = curr_frequency
			num = i

	return num

List = [2, 1, 2, 2, 1, 3]
Tuple = (1,1,2,2,1,3)

print("Most Common element from list:",most_frequent(List))
print("Most Common element from tuple:",most_frequent(Tuple))




