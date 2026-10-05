import argparse
import os
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

def execute_line(input_cmd, cmd_name):
    input_line = input_cmd.strip()

    if not input_line or input_line.startswith("#"):
        return False

    print(f"{cmd_name}:/$ {input_line}")

    parsed = input_line.split()
    command = parsed[0]
    arguments = parsed[1:]

    if command == "exit":
        print("Выход из эмулятора.")
        sys.exit(0)

    result = navigate(command, arguments)
    if result:
        print(result)
    return True

def main() -> int:

    parser = argparse.ArgumentParser(description="Эмулятор командной строки")
    parser.add_argument("--vfs", required=True, help="Путь к физическому расположению VFS")
    parser.add_argument("--script", help="Путь к стартовому скрипту для выполнения команд")

    args = parser.parse_args()
    cmd_name = "VFS"

    print("Отладочный вывод конфигурации")
    print(f"Путь к VFS: {os.path.abspath(args.vfs)}")
    print(f"Стартовый скрипт: {os.path.abspath(args.script) if args.script else 'Незадан'}")

    if args.script:
        if not os.path.exists(args.script):
            print(f"Ошибка: стартовый скрипт {args.script} не найден")
        else:
            print(f"Выполнение стартового скрипта: {args.script}")
            with open(args.script, "r") as f:
                for line in f:
                    execute_line(line, cmd_name)
            print("Выполнение стартового скрипта завершено")

    while True:
        try:
            cmd = input(cmd_name + ":/$ ")
            cmd = cmd.strip()

            if not cmd or cmd.startswith("#"):
                continue

            parsed = cmd.split()
            if not parsed:
                continue

            command = parsed[0]
            arguments = parsed[1:]

            if command == "exit":
                print("Выход из эмулятора.")
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