#Bloomberg ML intern coding question

#Given an array, try to push all the zero elements to the 
# end of the array without losing the relative order of the non-zero elements

#input = [-1, 0, 0, 3, 4, 2, 0, 6, 7, 0, 0, 0]
#output = [-1, 3, 4, 2, 6, 7, 0, 0 , 0, 0, 0, 0]

def main():
	input_list = raw_input("Please enter your inputs separated by commas (no spaces) and on the same line: ")
	input_list = [int(n) for n in input_list.split(',')]
	# print input_list
	count = 0 # Count of non-zero elements
	n = len(input_list)
    # While traversing array if element is non-zero, then
    # replace the element at index 'count' with this element
	for i in range(n):
		if input_list[i] != 0:  
			input_list[count] = input_list[i]
			count+=1 #increment count
	 
	# Make all remaining positions 0 from count to end.
	while count < n:
		input_list[count] = 0
		count += 1

	print input_list

if __name__ == '__main__':
	main()