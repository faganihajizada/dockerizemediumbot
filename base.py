from dbopr import dbopr

d = dbopr()

def my_method():

	select = int(raw_input('Enter 1 for userlist, 2 for add new user, 3 for enableuser and 4 for disable user '))

	if select == 1:

		userlist = d.get_userlist()
       		print(userlist)
		my_method()	

	elif select == 2:

       		username = raw_input('Add Medium Username: ')
		d.add_user(username)
		print("You add new user: ", username)
		my_method()	

	elif select == 3:

		enableuser = raw_input('Enable User: ')
		d.enable_user(enableuser)
		print("You enabled user: ", enableuser)
		my_method()	

	elif select == 4:

       		disableuser = raw_input('Disable User: ')
        	d.disable_user(disableuser)
        	print("You disabled user: ", disableuser)
		my_method()	

	else:

		my_method()	
		
my_method()		
