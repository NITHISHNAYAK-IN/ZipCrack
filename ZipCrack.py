#Free zip file cracker
#NITHISH NAYAK
#https://bit.ly/NITHISH-NAYAK-IN

from zipfile import ZipFile
import sys
import os

argv=False
try:
	if (sys.argv[1]=="-version" or sys.argv[1]=="--version"):
		print("Archive-PassCrack - version 1.0 Beta")
		argv=True
	else:
		pass
except:
	pass

def print_help():
	print("""
	
     This Tool Can Only Currently Extract Passwords of .ZIP
     Files.
     You Have To Just Specify The Zip File Path And Password List
     .TXT File.
	""")


try:
	if (sys.argv[1]=="-help" or sys.argv[1]=="--help"):
		print_help()
		argv=True
	else:
		pass
except:
	pass

if (argv==True):
	sys.exit()
else:
	pass

os.system("clear")


print("""
                 ZIP FILES CRACKER TOOL
""")

while(True):
	try:
		exit=False
		action=input("\nZip file > ")
		if(action=="quit"):
			exit=True
			break
		elif(action=="help"):
			print_help()
		else:
			pass
		try:
			zip=ZipFile(action,"r")
			break
		except:
			if(action=="" or action=="help"):
				pass
			else:
				print("\n\033[0;91m[!] Unable to locate the zip file!\033[0;0m")
	except:
		pass


if (exit==True):
	sys.exit()
else:
	pass

list=input("\nPassword list > ")

try:
	word=open(list,"rb")
	count=open(list,"r")
except:
	print("\n\033[0;91m[!] Unable to locate the password list!\033[0;0m")
	sys.exit()

print("\n")
line=count.readline()
condition=0
while(line):
	password=word.readline()
	try:
		zip.extractall(path="Extract",pwd=password.strip())
		print("\n[Password Found!] :: {}".format(password.decode()))
		condition+=1
		break
	except:
		print(password.decode())
	line=count.readline()
	
if(condition==0):
	print("\n[Password not found!]")
else:
	pass

zip.close()
word.close()
count.close()

