# Конфигурационное управление

## Практическая работа №1. 
## Вариант №11. Эмулятор для языка оболочки ОС

### Этап 1. REPL
1. Приложение реализовано в форме консольного интерфейса (CLI).
2. Приглашение к вводу содержит имя VFS: "VFS:/$".
3. Реализован простой парсер, который разделяет ввод на команду и аргументы по пробелам.
4. Реализованы команды-заглушки, которые выводят свое имя и аргументы: ls, cd.
5. Реализована команда exit.
6. Продемонстрированна работа всей реализованной функциональности прототипа в интерактивном режиме.
7. Результат выполнения этапа сохранен в репозиторий стандартно оформленным коммитом


Результат работы в интерактивном режиме:
```
VFS:/$ ls
ls []
VFS:/$ ls ssef sefs
ls ['ssef', 'sefs']
VFS:/$ cd
cd []
VFS:/$ cd dfsaf sf 
cd ['dfsaf', 'sf']
VFS:/$ exit
Process finished with exit code 0
```
---
### Этап 2. Конфигурация
1. Реализована поддержка параметров командной строки (`--vfs` и `--script`).
2. Организован автоматический отладочный вывод всех заданных конфигурационных параметров при старте приложения.
3. Стартовый скрипт поддерживает выполнение команд эмулятора последовательно, включая обработку комментариев (строки, начинающиеся с `#`). При выполнении скрипта имитируется интерактивный диалог (выводится и ввод, и вывод).
4. Написано несколько скриптов запуска реальной ОС для тестирования различных параметров командной строки.
5. Результат выполнения этапа сохранен в репозиторий стандартно оформленным коммитом.

#### Описание скриптов запуска реальной ОС (Покрытие параметров):
*   **`run_full.bat`** — Запуск эмулятора со всеми параметрами (передается и путь к файлу VFS, и путь к стартовому скрипту `start_script.txt`).
*   **`run_only_vfs.bat`** — Запуск эмулятора только с обязательным параметром `--vfs` напрямую в интерактивный режим (REPL).

#### Результат работы в интерактивном режиме (Этап 2 — Автоматический запуск скрипта):
```text
Параметры vfs, script
Отладочный вывод конфигурации
Путь к VFS: C:\Users\User\Documents\Конфигурационное управление\Conf_control_project\my_virtual_vfs
Стартовый скрипт: C:\Users\User\Documents\Конфигурационное управление\Conf_control_project\start_script.txt
Выполнение стартового скрипта: start_script.txt
VFS:/$ ls
ls []
VFS:/$ ls -la /var/log
ls ['-la', '/var/log']
VFS:/$ cd home/user/documents
cd ['home/user/documents']
Выполнение стартового скрипта завершено
VFS:/$ cd dfs/
cd ['dfs/']
VFS:/$ sfsa 
sfsa: команда не найдена
VFS:/$ ls sfs
ls ['sfs']
VFS:/$ exit
Выход из эмулятора.

Параметры vfs
Отладочный вывод конфигурации
Путь к VFS: C:\Users\User\Documents\Конфигурационное управление\Conf_control_project\my_virtual_vfs
Стартовый скрипт: Незадан
VFS:/$ exit
Выход из эмулятора.
```
---
### Этап 3. VFS (Виртуальная файловая система)
1. Подключена In-Memory VFS из JSON-файла `vfs_config.json`.
2. Реализованы команды навигации и вывода содержимого каталога (`ls`, `cd`, `cd ..`).
3. Динамически обновляется приглашение в командной строке.

```angular2html
Параметры vfs, script
Отладочный вывод конфигурации
Путь к VFS: C:\Users\User\Documents\Конфигурационное управление\Conf_control_project\vfs_config.json
Стартовый скрипт: C:\Users\User\Documents\Конфигурационное управление\Conf_control_project\start_script.txt
Выполнение стартового скрипта: start_script.txt
VFS:/$ ls
bin home
VFS:/$ cd home
VFS:/$ ls
user
VFS:/$ cd user/docs
VFS:/user/docs$ ls
readme.txt
VFS:/user/docs$ cd ..
VFS:/user$ ls
docs
VFS:/user$ cd
VFS:/$ cd /bin
VFS:/$ ls
VFS:/$ clear
clear: команда не найдена
VFS:/$ cd /home/user/invalid_folder
cd: /home/user/invalid_folder: Нет такого файла или директории
VFS:/$ cd bin
cd: bin: Нет такого файла или директории
VFS:/$ cd
Выполнение стартового скрипта завершено
VFS:/$
VFS:/$cd home/user/docs
VFS:/home/user/docs$cd
VFS:/$ls
bin home
VFS:/$cd bin
VFS:/bin$ls
VFS:/bin$ls
VFS:/bin$exit
Выход из эмулятора.
Press any key to continue . . . 
```
---
### Этап 4. Основные команды
1. Реализована логика для команд навигации и просмотра `ls` и `cd` в VFS.
2. Добавлены новые утилиты: `date` (дата/время MSK), `tree` (псевдографическое дерево) и `du` (размер элементов).
3. Обновлен стартовый скрипт `start_script.txt` и оформлен коммит.
```angular2html
Параметры vfs, script
Отладочный вывод конфигурации
Путь к VFS: C:\Users\User\Documents\Конфигурационное управление\Conf_control_project\vfs_config.json
Стартовый скрипт: C:\Users\User\Documents\Конфигурационное управление\Conf_control_project\start_script.txt
Выполнение стартового скрипта: start_script.txt
VFS:/$ ls
bin home
VFS:/$ cd home
VFS:/$ ls
user
VFS:/$ cd user/docs
VFS:/user/docs$ ls
readme.txt
VFS:/user/docs$ cd ..
VFS:/user$ ls
docs
VFS:/user$ cd
VFS:/$ cd /bin
VFS:/$ ls
VFS:/$ clear
clear: команда не найдена
VFS:/$ cd /home/user/invalid_folder
cd: /home/user/invalid_folder: Нет такого файла или директории
VFS:/$ cd bin
cd: bin: Нет такого файла или директории
VFS:/$ cd
VFS:/$ date
2026/10/06 17:16:26 MSK 2026
VFS:/$ tree
|--bin
^--home
    ^--user
        ^--docs
            ^--readme.txt
VFS:/$ du
bin: 0
home: 16
VFS:/$ cd home
VFS:/$ tree
^--user
    ^--docs
        ^--readme.txt
VFS:/$ du
user: 16
Выполнение стартового скрипта завершено
VFS:/home$cd
VFS:/$cd home/user
VFS:/home/user$ls
docs
VFS:/home/user$.\cd docs
.\cd: команда не найдена
VFS:/home/user$cd docs
VFS:/home/user/docs$ls
readme.txt
VFS:/home/user/docs$du
readme.txt: 16
VFS:/home/user/docs$cd 
VFS:/$exit
Выход из эмулятора.
Press any key to continue . .
```
---
## Запуск проекта и тестов
### Запуск проекта
```angular2html
./run_full.bat
```
### Команда для запуска автоматических Unit-тестов:
```bash
python -m unittest discover -s tests
```