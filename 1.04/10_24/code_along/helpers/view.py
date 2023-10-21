import os
from pathlib import Path


def windows_get_downloads():
    print("====PRINTING OUT FOLDERS OF 10_24====")
    path = "..\\1.04\\10_24"
    files = os.listdir(path)
    print(files)


def get_downloads():
    print("====PRINTING OUT FOLDERS OF 10_24====")
    path = Path("..", "1.04", "10_24")
    files = os.listdir(path)
    print(files)


def get_curr():
    print("====CURRENT DIRECTORY====")
    curr = os.getcwd()
    print(curr)


def get_home():
    print("====I KNOW YOUR HOME ADDRESS...DIRECTORY====")
    path = Path.home()
    print(path)


def make_adir():
    print("====MAKING A NEW FOLDER IN YOUR DESKTOP====")
    new_path = Path(Path.home(), "Desktop", "pokemon")
    new_path.mkdir()
    print(new_path)


if __name__ == "__main__":
    print("youve ran get_downloads")
    # sorry mac users
    windows_get_downloads()
    get_downloads()
    get_curr()
    get_home()
    # uncomment to make a pokemon dir
    # make_adir()
