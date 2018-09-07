#these are the data tools for the saulnet authentication system.

def hasher(uhash_pw): #check out the hashlib documentation for more
	algo = hashlib.sha256()
	algo.update(uhash_pw)
	hash_pw = algo.hexdigest()
	return hash_pw

def getdata(uname):
	get_user = ("SELECT * FROM users WHERE uname='%s'" % uname)
	crsr.execute(get_user)
	db_user_data = crsr.fetchall()
	#print(db_user_data) #comment out, for debugging purposes
	return db_user_data

def authenticator():
	uname = input('username:')
	db_user_data = getdata(uname)
	salt = db_user_data[0][2]
	uhash = db_user_data[0][3]
	guess = getpass.getpass('password (i hope it\'s a secret):')
	guess_hash_pw = binascii.unhexlify(salt) + str.encode(guess) #unhexlify turns the hex value from the db into a byte array for the hasher
	hash_pw = hasher(guess_hash_pw)
	if hash_pw == uhash:
		print("Authenticated!")		
		return
	else:
		print("Incorrect uname or pw")
		authenticator()