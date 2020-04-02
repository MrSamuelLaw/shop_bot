#!/usr/bin/env python3

import subprocess


def main():
    cmd = ['python', r'C:\Users\Samuel\Documents\CodingProjects\Python\in_progress\CNC_TOOLBOX\CNC_TOOLBOX\cnc_toolbox.py']
    for i in range(10):
        subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    main()
