import sys
import os
import ctypes
import random
import string
import time
from rich.progress import track

print("просмотр и проверка родительского хоста")
if os.path.isfile("D:\Project\Python\script\script_encoder\parent_host.dll"):
	print("просмотр и проверка хоста")
	if os.path.isfile("D:\Project\Python\script\script_encoder\host.dll"):
		print("")
	else:
		ctypes.windll.user32.MessageBoxW(0, "missing host", "error", 0)
		sys.exit()	
else:
	ctypes.windll.user32.MessageBoxW(0, "missing parent host", "error", 0)
	sys.exit()

directory = input("укажите directory - ")
print("1 - без шифравания")
print("2 - 1 архив")
print("3 - 2 архива")
print("4 - 3 архива")
method = input("укажите тип шифрования - ")
if method=='1':
	they = input("укажите куда хотите .ecd - ")
	os.rename(directory, they)
	exit(0)
if method=='2':
	def generate_random_string(length):
		letters = string.ascii_lowercase
		rand_string = ''.join(random.choice(letters) for i in range(length))
		print(rand_string)
	generate_random_string(20)
	print("\n\n\n")
	rar = input("куда сохраняете архив - ")
	they = input("укажите куда хотите .ecd - ")
	name = input("введите имя(название) - ")
	password = input("укажите пароль - ")
	os.renames(rar,they)
	with open(r'D:/project/python/script/script_encoder/password.txt', 'w') as fp:
		fp.write(password)
		pass
		
	with open(r'D:/project/python/script/script_encoder/configuration.txt','w') as fp:
		fp.write("")
		pass
		ctypes.windll.user32.MessageBoxW(0,'наберите 4 цифр по последовательности(без нуля)','please',0)
		os.startfile("D:/project/python/script/script_encoder/configuration.txt")
		time.sleep(2)
		print("\n\n\n\n")
		input("Для продолжения нажмите Enter")
		with open(r'D:/project/python/script/script_encoder/name.txt','w') as fp:
			fp.write(name)
			pass
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('1', '--------------------------------')
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('2',name)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('3', password)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('4', '--------------------------------')
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)
			input("Для продолжения нажмите Enter")
			print("\n\n\n")
			security = input("хотите ли вы зашифровать файлы конфиураций(y or n) - ")
			if security in ['y','Y','н','Н']:
				os.startfile('D:/project/python/script/script_encoder/rename.exe')
				time.sleep(2)
				os.startfile("D:/project/python/script/script_encoder/rename.pyc")
				os.startfile('D:/project/python/script/script_encoder/rename1.exe')
				lesson = input("хотите ли вы перекинуть файл .config(y or n) - ")
				if lesson in ['y','Y','н','Н']:
					time.sleep(5)
					os.startfile('D:/project/python/script/script_encoder/rename.exe')
					time.sleep(1)
					os.startfile("D:/project/python/script/script_encoder/rename.pyc")
					os.startfile('D:/project/python/script/script_encoder/path.pyc')
					exit(0)
				if lesson in ['n','N','т','Т']:
					time.sleep(5)
					os.startfile('D:/project/python/script/script_encoder/rename.exe')
					os.startfile("D:/project/python/script/script_encoder/rename.pyc")
					sys.exit()
				exit(0)
			if security in ['n','N','т','Т']:
				ctypes.windll.user32.MessageBoxW(0,'Ну ладно,как хочешь','',0)
				time.sleep(5)
				os.startfile('D:/project/python/script/script_encoder/rename.exe')
				os.startfile("D:/project/python/script/script_encoder/rename.pyc")
				lesson = input("хотите ли вы перекинуть файл .config(y or n) - ")
				if lesson in ['y','Y','н','Н']:
					time.sleep(1)
					os.startfile("D:/project/python/script/script_encoder/rename.pyc")
					os.startfile('D:/project/python/script/script_encoder/path.pyc')
					exit(0)
				if lesson in ['n','N','т','Т']:
					os.startfile("D:/project/python/script/script_encoder/rename.pyc")
					time.sleep(5)
					os.startfile('D:/project/python/script/script_encoder/rename.exe')
					sys.exit()
if method=='3':
	def generate_random_string(length):
		letters = string.ascii_lowercase
		rand_string = ''.join(random.choice(letters) for i in range(length))
		print(rand_string)
	generate_random_string(25)
	def generate_random_string(length):
		letters = string.ascii_lowercase
		rand_string = ''.join(random.choice(letters) for i in range(length))
		print(rand_string)
	generate_random_string(25)
	print("\n\n")
	rar = input("куда сохраняете архив - ")
	they = input("укажите куда хотите .ecd - ")
	password = input("укажите пароль - ")
	name = input("введите имя - ")
	password2 = input("укажите второй пароль - ")
	os.renames(rar,they)
	with open(r'D:/project/python/script/script_encoder/password.txt', 'w') as fp:
		fp.write(password)
		pass
		with open(r'D:/project/python/script/script_encoder/password2.txt','w') as fp:
			fp.write(password2)
			pass
			time.sleep(1)
	with open(r'D:/project/python/script/script_encoder/configuration.txt','w') as fp:
		fp.write("")
		pass
		ctypes.windll.user32.MessageBoxW(0,'наберите 5 цифр по последовательности(без нуля)','please',0)
		os.startfile("D:/project/python/script/script_encoder/configuration.txt")
		time.sleep(1)
		print("\n\n\n\n")
		input("Для продолжения нажмите Enter")
		with open(r'D:/project/python/script/script_encoder/name.txt','w') as fp:
			fp.write(name)
			pass
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('1', '--------------------------------')
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('2',name)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('3', password)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('4', password2)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)	
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('5', '--------------------------------')
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)
		os.startfile('D:/project/python/script/script_encoder/rename.exe')
		input("Для продолжения нажмите Enter")
		time.sleep(3)
		security = input("хотите ли вы зашифровать файлы конфиураций(y or n) - ")
		if security in ['y','Y','н','Н']:
			os.startfile('D:/project/python/script/script_encoder/rename.exe')
			time.sleep(4)
			os.startfile("D:/project/python/script/script_encoder/rename.pyc")
			os.startfile('D:/project/python/script/script_encoder/rename3.exe')
			lesson = input("хотите ли вы перекинуть файл .config(y or n) - ")
			if lesson in ['y','Y','н','Н']:
				time.sleep(4)
				os.startfile("D:/project/python/script/script_encoder/rename.pyc")
				os.startfile('D:/project/python/script/script_encoder/path.pyc')
				exit(0)
			if lesson in ['n','N','т','Т']:
				time.sleep(4)
				os.startfile("D:/project/python/script/script_encoder/rename.pyc")
				exit(0)
		if security in ['n','N','т','Т']:
			ctypes.windll.user32.MessageBoxW(0,'Ну ладно,как хочешь','',0)
			os.startfile('D:/project/python/script/script_encoder/rename.exe')
			time.sleep(4)
			os.startfile("D:/project/python/script/script_encoder/rename.pyc")
		lesson = input("хотите ли вы перекинуть файл .config(y or n) - ")
		if lesson in ['y','Y','н','Н']:
			time.sleep(4)
			os.startfile("D:/project/python/script/script_encoder/rename.pyc")
			os.startfile('D:/project/python/script/script_encoder/path.pyc')
			exit(0)
		if lesson in ['n','N','т','Т']:
			time.sleep(4)
			os.startfile("D:/project/python/script/script_encoder/rename.pyc")
			sys.exit()
		print("\n\n\n")
		exit(0)
if method=='4':
	def generate_random_string(length):
		letters = string.ascii_lowercase
		rand_string = ''.join(random.choice(letters) for i in range(length))
		print(rand_string)
	generate_random_string(25)
	print("\n\n")
	def generate_random_string(length):
		letters = string.ascii_lowercase
		rand_string = ''.join(random.choice(letters) for i in range(length))
		print(rand_string)
	generate_random_string(25)
	print("\n\n")
	def generate_random_string(length):
		letters = string.ascii_lowercase
		rand_string = ''.join(random.choice(letters) for i in range(length))
		print(rand_string)
	generate_random_string(25)
	print("\n\n")
	
	print("\n\n\n")
	rar = input("куда сохраняете архив - ")
	they = input("укажите куда хотите .ecd - ")
	name = input("введите имя - ")
	password = input("укажите пароль - ")
	password2 = input("укажите второй пароль - ")
	password3 = input("укажите третий пароль - ")
	os.renames(rar,they)
	with open(r'D:/project/python/script/script_encoder/password.txt', 'w') as fp:
		fp.write(password)
		pass
		with open(r'D:/project/python/script/script_encoder/password2.txt','w') as fp:
			fp.write(password2)
			pass
		with open(r'D:/project/python/script/script_encoder/password3.txt','w') as fp:
			fp.write(password3)
			pass
		with open(r'D:/project/python/script/script_encoder/configuration.txt','w') as fp:
			fp.write("")
			pass
		ctypes.windll.user32.MessageBoxW(0,'наберите 6 цифр по последовательности(без нуля)','please',0)
		os.startfile("D:/project/python/script/script_encoder/configuration.txt")
		time.sleep(1)
		print("\n\n\n\n")
		input("Для продолжения нажмите Enter")
		with open(r'D:/project/python/script/script_encoder/name.txt','w') as fp:
			fp.write(name)
			pass
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('1', '--------------------------------')
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('2',name)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('3', password)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('4', password2)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)	
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('5', password3)
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)	
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'r') as f:
			old_data = f.read()
			new_data = old_data.replace('6', '--------------------------------')
		with open ('D:/project/python/script/script_encoder/configuration.txt', 'w') as f:
			f.write(new_data)
		os.startfile("D:/project/python/script/script_encoder/rename.exe")
		input("Для продолжения нажмите Enter")
		time.sleep(3)
		security = input("хотите ли вы зашифровать файлы конфиураций(y or n) - ")
		if security in ['y','Y','н','Н']:
			os.startfile('D:/project/python/script/script_encoder/rename.exe')
			time.sleep(4)
			os.startfile("D:/project/python/script/script_encoder/rename.pyc")
			os.startfile('D:/project/python/script/script_encoder/rename5.exe')
			os.startfile('D:/project/python/script/script_encoder/rename7.exe')
			lesson = input("хотите ли вы перекинуть файл .config(y or n) - ")
			if lesson in ['y','Y','н','Н']:
				time.sleep(4)
				os.startfile("D:/project/python/script/script_encoder/rename.pyc")
				os.startfile('D:/project/python/script/script_encoder/path.pyc')
				exit(0)
			if lesson in ['n','N','т','Т']:
				time.sleep(4)
				os.startfile("D:/project/python/script/script_encoder/rename.pyc")
				sys.exit()
			exit(0)
		if security in ['n','N','т','Т']:
			ctypes.windll.user32.MessageBoxW(0,'Ну ладно,как хочешь','',0)
			os.startfile('D:/project/python/script/script_encoder/rename.exe')
			time.sleep(4)
			os.startfile("D:/project/python/script/script_encoder/rename.pyc")
			lesson = input("хотите ли вы перекинуть файл .config(y or n) - ")
			if lesson in ['y','Y','н','Н']:
				time.sleep(4)
				os.startfile("D:/project/python/script/script_encoder/rename.pyc")
				os.startfile('D:/project/python/script/script_encoder/path.pyc')
				exit(0)
			if lesson in ['n','N','т','Т']:
				time.sleep(4)
				os.startfile("D:/project/python/script/script_encoder/rename.pyc")
				sys.exit()
		
else:
	ctypes.windll.user32.MessageBoxW(0, "missing host", "error", 0)
	sys.exit()