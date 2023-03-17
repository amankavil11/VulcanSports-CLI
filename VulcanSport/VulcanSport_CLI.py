import argparse
from pathlib import Path
import subprocess

parser = argparse.ArgumentParser()

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
        args = ["python", "ls_argv.py", new_dir]
        process = subprocess.call(args)
        raise SystemExit(1)
    else:
        raise SystemExit(1)

max_len = max(len(entry.name) for entry in target_dir.iterdir())

for i, entry in enumerate(target_dir.iterdir()):
    if i % 2 == 0 and i != len(list(target_dir.iterdir()))-1:
        print(f"{entry.name: <{max_len}}", end='\t')
    else:
        print(entry.name)


