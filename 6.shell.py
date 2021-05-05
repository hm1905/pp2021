import os

print('testing: ')
home = ""
while 1:
    cmd = input(home+"> ")
    if cmd == "exit":
        break
    if cmd[:2] == "cd":
        home = cmd[3]
        os.chdir(cmd[3:])
    else:
        os.system(cmd)
