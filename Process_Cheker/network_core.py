import psutil
import time
import os
import sys

frames = ["|", "/", "-", "\\"]

def Process_check():
    print("=== КАКОЙ ИМЕННО ФАЙЛ НУЖНО ПРОВЕРИТЬ? ===\n")
    target_name = input("Введите имя процесса (например, chrome.exe): ").strip()
    
    if not target_name:
        print("Имя файла не может быть пустым\n")
        return
        
    print("=== ИЩУ ===\n")
    process_found = False
    
    if getattr(sys, 'frozen', False):
            current_dir = os.path.dirname(os.path.abspath(sys.executable))
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
    log_path = os.path.join(current_dir, "scan_report_choice_3.txt")
    
    with open(log_path, "w", encoding="utf-8") as log_file:
        log_file.write("=== ОТЧЁТ СКАНИРОВАНИЯ ЦЕЛЕВОГО ПРОЦЕССА ===\n")
        
        for p in psutil.process_iter(attrs=["pid", "name", "status"]):
            try:
                if p.info['name'].lower() == target_name.lower():
                    process_found = True
                    pid = p.info['pid']
                    name = p.info['name']
                    status = p.info['status']
                    
                    
                    for frame in frames:
                        print(f"\r[ {frame} ] Считываю структуры ОЗУ...", end="", flush=True)
                        time.sleep(0.05)
                    print("")
                    
                    print(f"\n[+] НАЙДЕН ПРОЦЕСС: {name} | PID: {pid} | Статус: {status}")
                    print("    Проверяю сетевую активность в ОЗУ...")
                    
                    log_file.write(f"\n[+] НАЙДЕН ПРОЦЕСС: {name} | PID: {pid} | Статус: {status}\n")
                    
                    connections = p.connections(kind='inet')
                    
                    if connections:
                        print(f"    [+] Активных сокетов обнаружено: {len(connections)}")
                        log_file.write(f"    Активных сокетов обнаружено: {len(connections)}\n")
                        
                        for conn in connections:
                            
                            print(f"    [+]  -> Локальный адрес: {conn.laddr}")
                            
                            log_file.write(f"      -> Локальный адрес: {conn.laddr}\n")
                            
                            if conn.raddr:
                                print(f"    [+]  -> Удаленный хост: {conn.raddr}")
                                
                                log_file.write(f"      -> Удаленный хост: {conn.raddr}\n")
                                
                            print(f"    [+]  -> Статус сокета: {conn.status}\n")
                            log_file.write(f"      -> Статус сокета: {conn.status}\n\n")
                    else:
                        print("    [-] Этот процесс сейчас не удерживает сетевые сокеты в памяти.\n")
                        log_file.write("    [-] Этот процесс сейчас не удерживает сетевые сокеты в памяти.\n")
                        
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

    
    if process_found:
        print("=== БЫЛ СОЗДАН ФАЙЛ В ПАПКЕ: [scan_report_choice_3.txt] ===\n")
    else:
        print(f"=== Ошибка: Процесс '{target_name}' прямо сейчас не запущен в ОЗУ Windows ===\n")
