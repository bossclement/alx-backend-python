import os
import subprocess


def fix_py_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                subprocess.run(["autopep8", "--in-place", file_path])


if __name__ == "__main__":
    directory = os.getcwd()
    fix_py_files(directory)
