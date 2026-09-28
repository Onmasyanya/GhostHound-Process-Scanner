import psutil


def path_check_name(target_name):
    try:
        print("\n[+] ИЩУ")
        if target_name.isdigit():
            print("[-] ОШИБКА: Ты ввёл цифры!\n")
            return
        for p in psutil.process_iter(attrs=["pid", "name", "status"]):     
                if p.info['name'].lower() == target_name.lower():
                        pid = p.info['pid']
                        proc = psutil.Process(pid)  
                        exe_path = proc.exe
                        print(f"\n[+] Процесс найден!\n")
                        print(f"\n[+] Имя: {proc.name()}\n")
                        print(f"\n[+] PID: {pid}\n")
                        print(f"\n[+] Путь: {exe_path()}\n")
                        return
        
    except psutil.NoSuchProcess:
        print("\n[-] Процесс уже закрылся или не существовал в ОЗУ.\n")
    except psutil.AccessDenied:
        print("\n[🚨 ОШИБКА]: Отказ в доступе! Запустите утилиту от Администратора\n")