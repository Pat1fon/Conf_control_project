import sys

def navigate(command, arguments):
    if command == "ls":
        return ls(arguments)
    elif command == "cd":
        return cd(arguments)
    else:
        return f"{command}: команда не найдена"

def ls (args):
    return f"ls {args}"

def cd (args):
    return f"cd {args}"

def main() -> int:

    cmd_name = "VFS"

    while True:
        try:
            cmd = input(cmd_name + ":/$ ")
            cmd = cmd.strip()

            parsed = cmd.split()
            if not parsed:
                continue

            command = parsed[0]
            arguments = parsed[1:]

            if command == "exit":
                sys.exit(0)

            result = navigate(command, arguments)
            if result:
                print(result)

        except (KeyboardInterrupt, EOFError) as err:
                    # Корректная обработка Ctrl+C или Ctrl+D
                    print(f"\nОшибка: {err}")
                    sys.exit(0)
    return 0

if __name__ == "__main__":
    main()