import os
import sys

def main():
    bad_hash = sys.argv[1]
    good_hash = sys.argv[2]
    os.system("git bisect start {bad_hash} {good_hash}")
    os.system("git bisect run python manage.py test")
    
if __name__ == '__main__':
    main()

