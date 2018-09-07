import os
import hashlib
import getpass #obfuscates password input
import sqlite3
import binascii #makes the hex returned from the db into byte array for hasher in the authenticator

import pwgen #i made this!

__doc__ = """

get a username and pw, salt the pw, hash salt and pw, store uname, salt, and pw into sql database
it prints the randomly-generated plain-english password

future: admin panel to directly manipulate database.

how to use: follow the prompts.

aug 2018

"""

#TODO add admin panel to manipulate db. consider making new lib for security purposes

conn = None
crsr = None
masterwordlist = None

def authenticator(uname):
	db_user_data = getdata(uname)
	#sqlite returns the row (immutable) within a list.
	salt = db_user_data[2]
	uhash = db_user_data[3]
	guess = getpass.getpass('password (i hope it\'s a secret):')
	guess_hash_pw = binascii.unhexlify(salt) + str.encode(guess) #unhexlify turns the hex value from the db into a byte array for the hasher
	hash_pw = hasher(guess_hash_pw)
	if hash_pw == uhash:
		#print("Authenticated!") #can uncomment to debug
		return True
	else:
		#print("Incorrect uname or pw") #can uncomment to debug
		return False

def checkuser(uname):
	if getdata(uname):
		return True
	else:
		return False

def hasher(uhash_pw): #check out the hashlib documentation for more
	algo = hashlib.sha256()
	algo.update(uhash_pw)
	hash_pw = algo.hexdigest()
	return hash_pw

def getdata(uname):
	get_user = ("SELECT * FROM users WHERE uname='%s'" % uname)
	crsr.execute(get_user)
	db_user_data = crsr.fetchone()
	#print(db_user_data) #comment out, for debugging purposes
	return db_user_data

def pwreset(uname):
	if checkuser(uname) == True:
		removeuser(uname)
		passmaker(uname)
		return
	else:
		return		

def main():
	while 1:
		print("pw system")
		print("1. passmaker")
		print("2. authenticator")
		print("3. resetter")
		print("q. quit")
		choice = input()
		if choice == 'q' or choice == 'Q':
			return
		uname = input("Username: ")
		if choice == "1":
			if checkuser(uname):
				print("User already exists!")
			else:
				passmaker(uname)
		elif choice == "2":
			if checkuser(uname):
				verified = authenticator(uname)
				if verified == True:
					print("Authenticated!")
				else:
					print("Incorrect username or password.")
			else:
				print("User not found!")
		elif choice == "3":
			if checkuser(uname):
				pwreset(uname)
			else:
				print("User not found!")
		else:
			"invalid input"

def passmaker(uname):
	word_string = pwgen.pwgen()
	unsec_pw = "{a}-{b}-{c}-{d}".format(a=word_string[0], b=word_string[1], c=word_string[2], d=word_string[3])
	print("your password is: %s" % unsec_pw)
	salt = os.urandom(256) #salt should be as long as the hash
	uhash_pw = salt + str.encode(unsec_pw) #converts to bytes for the hashing algo
	hash_pw = hasher(uhash_pw)
	user_data = uname, salt.hex(), hash_pw
	#so basically this is all based on string formatting because its based on data stored 
	#in a variable and not directly entered into a command.
	format_str = """INSERT INTO users (id, uname, salt, hash_pw)
					VALUES (NULL, "{uname}", "{salt}", "{hash_pw}");"""
	db_adduser = format_str.format(uname=user_data[0], salt=user_data[1], hash_pw=user_data[2])
	crsr.execute(db_adduser)
	conn.commit()
	del salt, uname, unsec_pw, uhash_pw, user_data
	#print("Hashed pw:")
	#print(hash_pw) #comment out, for debugging purposes
	return

def removeuser(uname):
	if checkuser(uname) == True:
		confirm = input("Type \"DELETE\" to delete user: ")
		if confirm == "DELETE":
			crsr.execute("DELETE FROM users WHERE uname='%s';" % uname)
			conn.commit()
			print("Deleted %s" % uname)
			return
		else:
			print("Delete cancelled.")
			return
	else:
		return
		
def startup():
	global conn
	global crsr
	global masterwordlist
	# open wordlist.txt from the root directory and adds it to the globally acessable masterwordlist for pw generation
	masterwordlist = pwgen.loadwordlist()
	if os.path.isfile("./users.db") == True:
		conn = sqlite3.connect('users.db')
		crsr = conn.cursor()
		return
	else:
		conn = sqlite3.connect('users.db')
		crsr = conn.cursor()
		db_createtable = """
			CREATE TABLE users ( 
			id INTEGER PRIMARY KEY, 
			uname VARCHAR(255), 
			salt BLOB,
			hash_pw BLOB);"""
		crsr.execute(db_createtable)
		return

####################################################################################################################################

startup()
main()
