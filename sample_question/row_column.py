"""find and takes the 2 digits, x,y as input and generates 2-dimensional array print.The input i-th row and j-th column"""

input_str = input()
dimensions=[int(x) for x in input_str.split(',')]

#assign a dimensions values

row_num=dimensions[0]
col_num=dimensions[1]

multi_list = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
	for col in range(col_num):
		multi_list[row][col]= row*col

#print list and array

print(multi_list)
