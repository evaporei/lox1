def run_file(filename: str):
    with open(filename, 'r') as f:
        source = f.read()
    run(source)

def run_prompt():
    while True:
        try:
            line = input('> ')
            if not line:
                continue
        except EOFError:
            break
        except KeyboardInterrupt:
            break
        run(line)

def run(source: str):
    print('woah, source:', source)
