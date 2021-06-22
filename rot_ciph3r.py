#python 3.6
import os, sys

def banner():
    print('''   __  ___  _       _       _     _____      
  /__\/ _ \| |_ ___/ |_ __ | |__ |___ / _ __ 
 / \// | | | __/ __| | '_ \| '_ \  |_ \| '__|
/ _  \ |_| | || (__| | |_) | | | |___) | |   
\/ \_/\___/ \__\___|_| .__/|_| |_|____/|_|   
                     |_| ''')
    print('\033[92m <@abdulconsole> \n \033[97m')
    print('This program is still under development.')
    print('='*50)
    
def clear():
    _ = os.system('clear' if os.name =='posix' else 'cls')
    
def rot(text, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for letter in text:
        output += alpha[(alpha.find(letter)+ index)%26]
    return output
    
def dec(ctext, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for letter in ctext:
        output += alpha[(alpha.find(letter)- index)%26]
    return output
    2
def main():
	while True:
		banner()
		print("Menu \n 1) Encrypt\n 2) Decrypt")
		ch = input(':')
		if(ch=='1'):
		    print('You are encrypting...')
		    raw_in = input('Enter the plaintext: ')
		    text = raw_in.lower()
		    index = int(input('Enter number of rotation: '))
		    print('Rot',index,': ',rot(text, index))
		elif(ch=='2'):
		    print("You are decrypting...")
		    raw_in = input('Enter the ciphertext: ')
		    text = raw_in.lower()
		    index = int(input('Enter number of rotation: '))
		    print('Rot',index,': ',dec(text, index))
		else:
		    print("Wrong entry")
		print('='*50)
		while True:
			answer = str(input('Restart?  y/n:'))
			if(answer != 'y'):
				#break
				sys.exit()
			clear()
			main()
main()