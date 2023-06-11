number_of_inputs=int(input("enter the number of inputs"))

if number_of_inputs !=9:
    print("invalid number of elements for a 3x3 matrix please run it again")
    exit()

matrix_list_1=[]
matrix_list_2=[]

for i in range(number_of_inputs):
    user_input_1 = input("Enter input {} for matrix 1: ".format(i+1))
    matrix_list_1.append(user_input_1)

print()

for i in range(number_of_inputs):
    user_input_2 = input("Enter input {} for matrix 2: ".format(i+1))
    matrix_list_2.append(user_input_2)

print("matrix_1 ={},{},{}\n\t  {},{},{}\n\t  {},{},{}".format(*matrix_list_1),"\n")
print("matrix_2 ={},{},{}\n\t  {},{},{}\n\t  {},{},{}".format(*matrix_list_2))

a = matrix_list_1
b = matrix_list_2

row_0_0=int(a[0])*int(b[0])+int(a[1])*int(b[3])+int(a[2])*int(b[6])       
row_0_1=int(a[0])*int(b[1])+int(a[1])*int(b[4])+int(a[2])*int(b[7])
row_0_2=int(a[0])*int(b[2])+int(a[1])*int(b[5])+int(a[2])*int(b[8])

row_1_0=int(a[3])*int(b[0])+int(a[4])*int(b[3])+int(a[5])*int(b[6])
row_1_1=int(a[3])*int(b[1])+int(a[4])*int(b[4])+int(a[5])*int(b[7])
row_1_2=int(a[3])*int(b[2])+int(a[4])*int(b[5])+int(a[5])*int(b[8])

row_2_0=int(a[6])*int(b[0])+int(a[7])*int(b[3])+int(a[8])*int(b[6])
row_2_1=int(a[6])*int(b[1])+int(a[7])*int(b[4])+int(a[8])*int(b[7])
row_2_2=int(a[6])*int(b[2])+int(a[7])*int(b[5])+int(a[8])*int(b[8])

print("{} {} {}".format(row_0_0,row_0_1,row_0_2))
print("{} {} {}".format(row_1_0,row_1_1,row_1_2))
print("{} {} {}".format(row_2_0,row_2_1,row_2_2))




