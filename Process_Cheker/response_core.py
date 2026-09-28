import os
import sys
import winreg
import psutil

def eliminate_malware_threat(target_pid, registry_name=None, file_path=None):
    print(f"\n[🚨 RESPONS SVC]: Начинаю экстренное уничтожение угрозы...")
    try:
        
        process = psutil.Process(target_pid)
        p_name = process.name()
        
        print(f"\n[*] Выгружаю процесс {p_name} (PID: {target_pid}) из ОЗУ...")
        
        process.kill()
        print("\n[+] Процесс успешно ликвидирован.")

            
        if registry_name:
            try:
                path_run = r"Software\Microsoft\Windows\CurrentVersion\Run"

                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path_run, 0, winreg.KEY_SET_VALUE)
                
                print(f"[*] Удаляю параметр '{registry_name}' из автозагрузки реестра...")
                
                winreg.DeleteValue(key, registry_name)
                winreg.CloseKey(key)
                print("\n[+] Запись в реестре успешно уничтожена.")
                
            except OSError as e:
                print(f"\n[-] Не удалось удалить ключ из реестра (возможно, его там и не было): {e}")

               
        if file_path:
            try:
                print(f"\n[*] Физически стираю файл с жёсткого диска: {file_path}...")
                
                os.remove(file_path)
                print("\n[+] Фредоносный файл успешно стёрт с диска.")
                return True
                
            except OSError as e:
                print(f"\n[-] Не удалось удалить файл с диска (возможно, файл заблокирован или уже удалён): {e}\n")
                return False
                
        return True

    except psutil.NoSuchProcess:
        print("\n[-] Процесс уже закрылся или не существовал в ОЗУ.\n")
    except psutil.AccessDenied:
        print("\n[🚨 ОШИБКА]: Отказ в доступе! Запустите утилиту от Администратора для убийства процесса.\n")
        return False