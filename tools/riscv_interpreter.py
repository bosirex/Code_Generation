WeChat: cstutorcs
QQ: 749389476
Email: tutorcs@163.com
#!/usr/bin/env python3
"""
This script calls 'python3 -m riscemu' with the right options,
and removes the additional prints created by riscemu.
With this script, we only have the output generated by the program file, and
additionally have one line for the return code.
"""

import subprocess
import argparse

from riscv.parser import *


def __main__():
    parser = argparse.ArgumentParser(description='A RISC-V interpreter')
    parser.add_argument('file', type=argparse.FileType('r'))
    args = parser.parse_args()
    result = subprocess.run(["python3", "-m", "riscemu", args.file.name],
                            capture_output=True)
    print(result.stdout.decode("ascii"))
    print(f"Return code: {result.returncode}")
    print(f"Interpreter Errors: {result.stderr.decode('utf8')}")


if __name__ == "__main__":
    __main__()