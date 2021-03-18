from os import system

files = ['compute','constant','mathFunc','mySys','temp']

def getCommand():
    '''derive command.'''
    command = input('>> ') # command prompt
    if command and command[-1] == ':': # mutiple-line prompt
        command = multiLine(command)
    return command

def multiLine(head=''):
    '''derive multiple-lines derive.'''
    command = [head]
    while True:
        line = input('...') # mutiple-line prompt
        if not line:
            break
        command.append(line)
    return '\n'.join(command)

def open(file='constant.py'):
    '''opend file with notepad.'''
    system('start notepad %s' % file)

def openAll():
    '''open all py files.'''
    for file in files:
        system('start notepad %s.py' % file)
