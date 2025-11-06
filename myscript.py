import os
import sys

def main():
    if len(sys.argv) != 3:
        print("wrong number of arguments")
        sys.exit(1)

    bad_hash = sys.argv[1]
    good_hash = sys.argv[2]

    os.system(f"git bisect start {bad_hash} {good_hash}")
    os.system("git bisect run python manage.py test")

if __name__ == "__main__":
    main()
