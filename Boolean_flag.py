#encoding:utf-8
#set the real password
real_pwd = 'abc123'

#set a boolean flag 'False' , GIVE A INITIAL VALUE FOR BOOLEAN FLAG
pwd_match = False

#create a while loop for checking the password entered by users
while not pwd_match:
	pwd = input('Please enter your password: ')
	if real_pwd == pwd :
		print('Thank U! You have entered the correct password!')
		pwd_match = True #Can't use 'Space' to aling the space of 'tab'
	else :
		print('Sorry, the string entered in incorrect -- try again')