#encoding:utf-8
#Get string from user
input_string = input('Please Enter String: ')

#let the position 3 is an A
output_string = input_string[:2] + 'A' + input_string[3:]

#print out the output
print(output_string)
