#encoding:utf-8
text = 'Python is a programming language, just like C,C++,Java,Python,R. '
text += 'Python.. is also a kind of snack. '
text += 'Uhh..no no! Python is snake, not snack. Python belongs to pythonidae. '
text += 'Have you understand Python? '

punc = [ ',' , '.' , '?' , '!' ]
for p in punc:
	text = text.replace(p,' ') #eliminate all the punctuations

parsed = text.split()
count_python, count_python_is = 0, 0
for i in range(len(parsed)):
	if parsed[i].count('Python') >= 1:
		count_python += 1
		if i+1 == len(parsed):
			break
		elif parsed[i+1] == 'is':
			count_python_is += 1

print(count_python_is)
print(count_python)
print('P(\'Python is\' | \'Python\'): %.2f ' %(float(count_python_is)/float(count_python)) )
print(float(count_python_is)/float(count_python))