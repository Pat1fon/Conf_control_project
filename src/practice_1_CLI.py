import argparse
import os
import sys
import json
from datetime import datetime

vfs_tree = {}
current_path = []

def get_node_by_path(path_list):
    #Служебная функция для получения узла JSON-дерева по списку путей
    node = vfs_tree

    for dir_name in path_list:
        if isinstance(node, dict) and dir_name in node:
            node = node[dir_name]
        else:
            return None
    return node

def navigate(command, arguments):
    global current_path
    if command == "ls":
        return ls(arguments)
    elif command == "cd":
        return cd(arguments)
    elif command == "date":
        return date_cmd(arguments)
    elif command == "tree":
        return tree_cmd(arguments)
    elif command == "du":
        return du_cmd(arguments)
    else:
        return f"{command}: команда не найдена"

def ls (args):
    node = get_node_by_path(current_path)
    if not isinstance(node, dict):
        return "Ошибка: текущая директория повреждена"

    items = list(node.keys())
    return " ".join(items) if items else ""

def cd (args):
    global current_path

    if not args:
        current_path = []
        return ""

    target_path = args[0]

    if target_path == "..":
        if len(current_path) > 0:
            current_path.pop()
        return ""

    segments = [s for s in target_path.split("/") if s]

    new_path = segments if target_path.startswith("/") else current_path + segments

    node = get_node_by_path(new_path)
    if node is None or not isinstance(node, dict):
        return f"cd: {target_path}: Нет такого файла или директории"

    current_path = new_path
    return ""

def date_cmd(arguments):
    #Реализация команды date
    return datetime.now().strftime("%Y/%m/%d %H:%M:%S MSK %Y")

def _build_tree(node, prefix=""):
    #Рекурсивная функция отрисовки дерева
    if not isinstance(node, dict):
        return []
    lines = []
    items = list(node.keys())

    for i, item in enumerate(items):
        connector = "^--" if i == len(items) - 1 else "|--"
        lines.append(f"{prefix}{connector}{item}")

        if isinstance(node[item], dict):
            new_prefix = prefix + ("    " if i == len(items) - 1 else "|   ")
            lines.extend(_build_tree(node[item], new_prefix))
    return lines

def tree_cmd(arguments):
    # Реализация команды tree
    node = get_node_by_path(current_path)
    if not isinstance(node, dict):
        return "Ошибка: невозможно построить дерево"
    lines = _build_tree(node)
    return "\n".join(lines) if lines else "."

def _calculate_size(node):
    # Рекурсивный подсчет размера файлов
    if not isinstance(node, dict):
        return len(str(node))
    total = 0
    for item in node.values():
        total += _calculate_size(item)
    return total

def du_cmd(arguments):
    # Реализация команды du
    node = get_node_by_path(current_path)
    if not isinstance(node, dict):
        return "Ошибка: невозможно рассчитать размер"

    lines = []
    for item_name, item_value in node.items():
        size = _calculate_size(item_value)
        lines.append(f"{item_name}: {size}")
    return "\n".join(lines) if lines else ""


def execute_line(input_cmd, cmd_name):
    input_line = input_cmd.strip()

    if not input_line or input_line.startswith("#"):
        return False

    vfs_display_path = "/" + "/".join(current_path[1:])
    print(f"{cmd_name}:{vfs_display_path}$ {input_line}")

    parsed = input_line.split()
    if not parsed:
        return False
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

    global vfs_tree

    parser = argparse.ArgumentParser(description="Эмулятор командной строки")
    parser.add_argument("--vfs", required=True, help="Путь к физическому расположению VFS")
    parser.add_argument("--script", help="Путь к стартовому скрипту для выполнения команд")

    args = parser.parse_args()
    cmd_name = "VFS"

    print("Отладочный вывод конфигурации")
    print(f"Путь к VFS: {os.path.abspath(args.vfs)}")
    print(f"Стартовый скрипт: {os.path.abspath(args.script) if args.script else 'Незадан'}")

    try:
        with open(args.vfs, "r", encoding="utf-8") as f:
            vfs_tree = json.load(f)
    except Exception as e:
        print(f"Критическая ошибка загрузки VFS: {e}")
        sys.exit(1)

    if args.script:
        if not os.path.exists(args.script):
            print(f"Ошибка: стартовый скрипт {args.script} не найден")
        else:
            print(f"Выполнение стартового скрипта: {args.script}")
            with open(args.script, "r", encoding="utf-8") as f:
                for line in f:
                    execute_line(line, cmd_name)
            print("Выполнение стартового скрипта завершено")

    while True:
        try:
            vfs_display_path = "/" + "/".join(current_path)

            cmd = input(f'{cmd_name}:{vfs_display_path}$')
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
