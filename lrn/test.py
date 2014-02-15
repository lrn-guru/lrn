import os

while True:
	cmd = raw_input("> ")
	if cmd.startswith('vim'):
		os.system(cmd)
	else:
		print('enter vim')

print('hi')
