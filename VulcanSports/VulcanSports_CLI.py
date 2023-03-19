import argparse
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser(prog="VulcanSports")

parser.add_argument("path", nargs="?", const=" ", default=" ")

parser.add_argument("-p", "--parent", action="store_true", help="list files in parent directory")

args = parser.parse_args()
if args.path == " ":
    args.path = "."

if args.parent:
    args.path = ".."
    
target_dir = Path(args.path).expanduser() #allows for use of tilde paths


if not target_dir.is_dir():
    print("The target directory doesn't exist")
    x = input("Try again(y/n)?: ")
    if (x).lower() == 'y':
        print()
        new_dir = input('New directory path?: ')
        args = ["python", "-m","VulcanSports", new_dir]
        process = subprocess.call(args)
        raise SystemExit(1)
    else:
        raise SystemExit(1)


max_len = max(len(entry.name) for entry in target_dir.iterdir())
entries = list(target_dir.iterdir())

if max_len < 50:
    for i in range(len(entries)-1):
        if i % 2 == 0:
            print(f"{entries[i].name: <{max_len}}", end='\t')
        else:
            print(entries[i].name)
    print(entries[-1].name)
else:
    for entry in entries:
        print(entry.name)


