import os
import repl
import sys

def main():
    user = os.geteuid
    print('user id is {}',user)
    repl.Repl().start(sys.stdin,sys.stdout)

if __name__ == "__main__":
    main()