import sys
from pathlib import Path
from colorama import init, Fore

init(autoreset=True)

def show_tree(path, indent=""):

    try:
        for item in path.iterdir():
            if item.is_dir():
                print(indent + Fore.BLUE + item.name + "/")
                show_tree(item, indent + " ")
            else:
                print(indent + Fore.GREEN + item.name)
    except Exception as e:
        print(Fore.RED + f"Error: {e}")
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please enter the directory path")        
        sys.exit()
    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print("Path does not exist")
        sys.exit()
    if not dir_path.is_dir():
        print("This is not a directory")
        sys.exit()
    
    print("Directory content:\n")
    show_tree(dir_path)