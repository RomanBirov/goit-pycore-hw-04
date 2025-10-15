import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

DIR_COLOR = Fore.CYAN + Style.BRIGHT
FILE_COLOR = Fore.GREEN
ERROR_COLOR = Fore.RED + Style.BRIGHT
FAINT = Style.DIM

BRANCH = "┣━ "
LAST_BRANCH = "┗━ "
VERT = "┃  "
SPACE = "   "

def print_tree(root: Path, prefix: str = "") -> None:
    try:
        items = sorted(root.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except PermissionError:
        print(prefix + ERROR_COLOR + "[Forbidden]")
        return

    count = len(items)
    for i, p in enumerate(items):
        is_last = (i == count - 1)
        branch = LAST_BRANCH if is_last else BRANCH
        next_prefix = prefix + (SPACE if is_last else VERT)

        if p.is_dir():
            print(prefix + branch + DIR_COLOR + f"{p.name}/")
            print_tree(p, next_prefix)
        else:
            print(prefix + branch + FILE_COLOR + p.name)

def main():
    if len(sys.argv) != 2:
        print(ERROR_COLOR + "ERROR: no directory path as argument")
        sys.exit(1)

    root = Path(sys.argv[1])

    if not root.exists():
        print(ERROR_COLOR + f"ERROR: path does not exist {root}")
        sys.exit(1)

    if not root.is_dir():
        print(ERROR_COLOR + f"ERROR: no directory {root}")
        sys.exit(1)

    print(DIR_COLOR + f"{root.resolve().name}/")
    print_tree(root)

if __name__ == "__main__":
    main()