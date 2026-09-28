import winreg
import os
import sys

def get_autostart_paths():
    print("=== АУДИТ ВЕТКИ АВТОЗАГРУЗКИ REGISTRY ===")
    
    path_run = r"Software\Microsoft\Windows\CurrentVersion\Run"
    
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, path_run, 0, winreg.KEY_READ)
        
        index = 0
        
        while True:
            try:
                name, value, _ = winreg.EnumValue(key, index)
                
                print(f"[+] Программа: {name}")
                print(f"[+]  Путь запуска: {value}\n")
                
                index += 1
                
            except OSError:
                break
                
        winreg.CloseKey(key)
        
    except OSError as e:
        print(f"[-] Ошибка доступа к реестру Windows: {e}")
