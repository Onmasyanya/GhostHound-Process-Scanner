import psutil
import os
import sys

def show_process_network():
    print("=== АУДИТ СЕТЕВЫХ СОКЕТОВ В ОЗУ ===")
    
    if getattr(sys, 'frozen', False):
        current_dir = os.path.dirname(os.path.abspath(sys.executable))
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
            
    log_path = os.path.join(current_dir, "scan_report_socket_choice_2.txt")
    
    
    with open(log_path, "w", encoding="utf-8") as log_file:
        log_file.write("=== ОТЧЁТ СКАНИРОВАНИЯ ВСЕХ ПРОЦЕССОВ ===\n\n")
        
        for process in psutil.process_iter(attrs=['pid', 'name']):
            try:
                connections = process.connections(kind='inet')
                if connections:
                    
                    p_name = process.info['name']
                    p_pid = process.info['pid']
                    
                    for conn in connections:
                        
                        
                        
                        log_file.write(f"Процесс: {p_name} | PID: {p_pid} | Статус: {conn.status} | Локал: {conn.laddr} | Удаленный: {conn.raddr}\n")
                        print(f"[+] ПРОЦЕСС: {p_name} | PID: {p_pid} | STATUS: {conn.status} | LOCAL: {conn.laddr} | ROOT: {conn.raddr}\n")
                        
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
                
   
    print("=== ОТЧЁТ УСПЕШНО СОХРАНЁН В ФАЙЛ scan_report_socket_choice_2.txt ===\n")
