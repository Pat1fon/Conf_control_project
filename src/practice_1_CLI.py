import sys

def navigate(command, arguments):
    if command == "ls":
        ls(arguments)
    elif command == "cd":
        cd(arguments)

def ls (args):
    print(f"ls {args}")

def cd (args):
    print(f"cd {args}")

def main() -> int:

    cmd_name = "VFS"

    while True:
        try:
            cmd = input(cmd_name + ":/$ ")
            cmd = cmd.strip()

            parsed = cmd.split()
            command = parsed[0]
            arguments = parsed[1:]

            if cmd == "exit":
                sys.exit(0)

            navigate(command, arguments)

        except (KeyboardInterrupt, EOFError) as err:
                    # Корректная обработка Ctrl+C или Ctrl+D
                    print(f"\nОшибка: {err}")
                    sys.exit(0)

if __name__ == "__main__":
    main()