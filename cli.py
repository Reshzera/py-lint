# cli.py
import sys
from linter.runner import check_file

def main():
    if len(sys.argv) < 2:
        print("Uso: python cli.py [arquivos.py]")
        sys.exit(1)

    for filename in sys.argv[1:]:
        problems = check_file(filename)
        if not problems:
            print(f"{filename}: Nenhum problema encontrado.")
        else:
            for p in problems:
                print(f"{p['filename']}:{p['lineno']}: {p['message']}")

if __name__ == "__main__":
    main()
