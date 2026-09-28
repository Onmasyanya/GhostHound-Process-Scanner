import psutil
import os
import sys

def show_windows_processes():
    print("=== АУДИТ ВСЕХ ПРОЦЕССОВ В ОЗУ ===")
    if getattr(sys, 'frozen', False):
        current_dir = os.path.dirname(os.path.abspath(sys.executable))
    else:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
    log_path = os.path.join(current_dir, "scan_report_process_choice_1.txt")
    
    
    with open(log_path, "w", encoding="utf-8") as log_file:
        log_file.write("=== ОТЧЁТ СКАНИРОВАНИЯ ВСЕХ ПРОЦЕССОВ ===\n\n")
        
        
        for process in psutil.process_iter(attrs=['pid', 'name', 'status']):
            try:
                p_info = process.info
                pid = p_info['pid']
                name = p_info['name']
                status = p_info['status']
                
                
                print(f"ID: {pid} | Имя: {name} | Статус: {status}")
                
                
                log_file.write(f"[+] Найдена цель: {name} | PID: {pid} | СТАТУС: {status}\n")
                
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
                
    
    print("\n[+] === ОТЧЁТ УСПЕШНО СОХРАНЁН В scan_report_process_choice_1.txt ===")
