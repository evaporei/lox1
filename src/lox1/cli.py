def run_file(filename: str):
    try:
        with open(filename, 'r') as f:
            source = f.read()
        run(source)
    except FileNotFoundError as err:
        print(err)

def run_prompt():
    while True:
        try:
            line = input('> ')
            if not line:
                continue
        except (EOFError, KeyboardInterrupt):
            break
        run(line)

def run(source: str):
    print('woah, source:', source)
