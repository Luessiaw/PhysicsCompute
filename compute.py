from constant import *
from mySys import getCommand, open, openAll
from mathFunc import *

def main():
    print('Physical Compute Tool by Luessiaw')
    while True:
        command = getCommand()
        Except = False
        try:
            result = eval(command) 
            if result != None:
                print(result)
        except:
            Except = True
        if Except:
            try:
                exec(command)
            except Exception as Except:
                print(type(Except),Except)

if __name__ == '__main__':
    main()
