import os
import sys

def main():
    if len(sys.argv) != 3:
        print("Wrong number of arguments")
        sys.exit(1)

    bad_hash = sys.argv[1]
    good_hash = sys.argv[2]

    os.system(f"git bisect start {bad_hash} {good_hash}")
    exit_code = os.system("git bisect run python manage.py test > bisect_log.txt 2>&1")

    with open("bisect_log.txt", "r", encoding="utf-8") as f:
        log = f.read()

    if "is the first bad commit" in log:
        bad_line = [line for line in log.splitlines() if "is the first bad commit" in line][0]
        print(f"Bisect found a bad commit: {bad_line}")
        sys.exit(1)
    elif exit_code != 0:
        print("Bisect failed due to an error in tests or setup.")
        sys.exit(1)
    else:
        print("No bad commit found.")
        sys.exit(0)

if __name__ == "__main__":
    main()
