# cli.py
import sys
from linter.runner import check_file

def main():
    print("PY_LINT: START_LINT")
    if len(sys.argv) < 2:
        print("Uso: python cli.py [file.py]")
        sys.exit(1)

    for filename in sys.argv[1:]:
        problems = check_file(filename)
        if not problems:
            print(f"{filename}: No problem found.")
        else:
            for p in problems:
                print(f"{p['filename']}:{p['lineno']}:{p['col_offset']}-{p['end_col_offset']}: {p['message']}")
    print("PY_LINT: END_LINT")

if __name__ == "__main__":
    main()
