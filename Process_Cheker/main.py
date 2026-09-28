import psutil
import time
import winreg
import sys
import os
import re


from process_core import show_windows_processes # Все процессы

from network_general import show_process_network # Все аудиты сокетов

from network_core import Process_check # Чекер одного процесса

from registry_core import get_autostart_paths # Чекер автозагрузки

from memory_core import dump_process_strings # Дампер ОЗУ

from response_core import eliminate_malware_threat #Экстренный убийца процесса(уничтожает файл полностью с выбранным PID)

from path_check_name import path_check_name # Чекер пути процесса по имени

from path_check_pid import path_check_pid # Чекер пути процесса по PID

if __name__ == "__main__":
    while True:
        print("Выбери режим аудита Windows:")
        print("1 — Общий список процессов (Имя, Статус)")
        print("2 — Детальный аудит сетевых сокетов в ОЗУ")
        print("3 - Выбор ОДНОГО процесса (Имя, Статус, Айди, Детальный аудит сетевых сокетов в ОЗУ)")
        print("4 - Сканирование автозагрузки")
        print("5 — Дамп строк из ОЗУ процесса (String Extraction)")
        print("6 - Нахождение пути (откуда файл)")
        print("7 - Ликвидация выбранной угрозы")
        print("0 - Выход из программы")
        
        choice = input("Введи цифру режима: ")
        
        if choice == "1":
            show_windows_processes()

        elif choice == "2":
            show_process_network()

        elif choice == "3":
            Process_check()

        elif choice == "4":
            get_autostart_paths()

        elif choice == "5":
            target_pid = input("Введите PID процесса для дампа памяти: ").strip()
            if not target_pid.isdigit():
                print("Ошибка: PID должен состоять только из цифр.\n")
                continue
            dump_process_strings(int(target_pid))

        elif choice == "6":
            print("\n=-= НАХОЖДЕНИЕ ПУТИ ГДЕ ЛЕЖИТ ФАЙЛ =-=")
            choice_six = input("Введите как хотите найти путь процесса? (по PID - 1, по ИМЕНИ - 2): ").strip()
            if choice_six == "1":
                pid_proc = input("\nВведите PID процесса: ")
                if not pid_proc.isdigit():
                    print("Ошибка: PID должен состоять только из цифр.\n")
                    continue
                path_check_pid(int(pid_proc))
            elif choice_six == "2":
                target_name = input("\nВведи имя процесса(Пример: firefox.exe): ")
                if target_name == "":
                    continue
                path_check_name(str(target_name))
            else:
                print("\n[-] Неправильно действие! Выбери строго между 1 и 2\n")

        elif choice == "7":
            print("-=- РЕЖИМ: ЛИКВИДАЦИЯ УГРОЗЫ -=-")
            kill_pid = input("Введите PID процесса для его полного уничтожения: ").strip()
            if not kill_pid.isdigit():
                print("Ошибка: PID должен состоять только из цифр.\n")
                continue

            reg_name = input("Введите имя параметра в реестре для удаления (Если нет - нажмите Enter): ").strip()
            if reg_name == "":
                reg_name = None

            f_path = input("Введите полный путь к файлу для удаления (если нет - нажмите Enter): ")
            if f_path == "":
                f_path = None

            eliminate_malware_threat(int(kill_pid), registry_name=reg_name, file_path=f_path)
        elif choice == "0":
            break
        else:
            print("Ошибка: выбран несуществующий режим.")

input("Нажмите Enter для выхода")