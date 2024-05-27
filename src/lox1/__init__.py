import sys
from lox1 import cli

def main() -> int:
    if len(sys.argv) > 2:
        print("Usage: plox [script]")
        return 64
    if len(sys.argv) == 2:
        cli.run_file(sys.argv[1])
    else:
        cli.run_prompt()
    return 0
