import psutil


def path_check_pid(pid_proc):
        try:
                proc = psutil.Process(pid_proc)
                exe_path = proc.exe
                print(f"\n[+] Процесс найден!\n")
                print(f"\n[+] Имя: {proc.name()}\n")
                print(f"\n[+] Путь: {exe_path()}\n")
                return

        except psutil.NoSuchProcess:
            print("\n[-] Процесс уже закрылся или не существовал в ОЗУ.\n")
        except psutil.AccessDenied:
            print("\n[🚨 ОШИБКА]: Отказ в доступе! Запустите утилиту от Администратора\n")