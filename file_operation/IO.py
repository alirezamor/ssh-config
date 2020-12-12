_configs = []

def get_config(path):
	try:
		f = open(path)

		lines = f.readlines()

		pages = []

		page = 0
		temp = []
		for index in range(len(lines)):
			if((lines[index][0]=='#' and lines[index][1] != ' ') or 'A' <= lines[index][0] <= 'Z' or 'A' <= lines[index][0] <= 'Z'):
				if(lines[index][len(lines[index])-1] == '\n'):
					_configs.append(lines[index].replace('\n', ''))
				#configs.append(lines[index])
			if(lines[index] == "\n"):
				pages.append(temp)
				temp = []
				page += 1
				continue
			temp.append(lines[index])
		f.close()
	except FileNotFoundError as e:
		print("File Not Found")

	return _configs

def write_into_file(configs):
	f = open("/home/alireza/DevOps/test.txt", "w")
	for config in configs:
		config += '\n'
		f.write(config)

def print_configs():
	if _configs:
		counter = 0
		for config in _configs:
			print(f"{counter}. {config}")
			counter+=1

def print_updated_configs(configs):
	if configs:
		counter = 0
		for config in configs:
			print(f"{counter}. {config}")
			counter+=1