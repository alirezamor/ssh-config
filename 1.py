from file_operation import IO as io
import os

def menu():
    print("1. uncomment")
    print("2. comment")
    print("3. update")
    print("4 -1. exit")
    print("enter your choice and index")

def clear():
    print("\n" * 100)


configs = io.get_config("/etc/ssh/sshd_config")
io.print_configs()

flag = True

menu()
choice, index = map(int, input().split())

while(flag):
    if choice == 1: #uncomment config
        if configs[index][0] == '#':
            configs[index] = configs[index].replace('#', '')
            clear()
            print("done")
            
        else:
            clear()
            print("it was uncommented")

    if choice == 2: #comment config
        if configs[index][0] != '#':
            configs[index] = "#" + configs[index]
            clear()
            print("done")
            
        else:
            clear()
            print("it was commented")
            
    if choice == 3: #update config
        if index == -1:
            io.write_into_file(configs)
        else:
            clear()
            print("enter your value")
            value = input()
            configs[index] = configs[index][0 : configs[index].find(" ")] + " " + value
            io.write_into_file(configs)
        

    if choice == 4 and index == -1: #update config
        flag = False
    
    if choice > 4 or choice < 1:
        clear()
        
    menu()
    choice, index = map(int, input().split())
