import os


def main():
	try:
		# os.environ['OLD_PS1'] = os.environ['PS1']
		# os.environ['PS1'] = 'lrn: ' + os.environ['PS1']
		while True:
			cmd = raw_input("lrn > ")
			os.system(cmd)
	except EOFError:
		print('Exiting lrn...')
		exit(0)
		# os.environ['PS1'] = os.environ['OLD_PS1']



if __name__ == '__main__':
	main()


