import ctypes
import psutil
import re

kernel32 = ctypes.windll.kernel32
PROCESS_ACCESS_FLAGS = 0x0010 | 0x0400

def dump_process_strings(target_pid):
    print(f"=== АУДИТ ВИРТУАЛЬНОЙ ПАМЯТИ PID: {target_pid} ===")
    
    process_handle = kernel32.OpenProcess(PROCESS_ACCESS_FLAGS, False, target_pid)
    
    if not process_handle:
        print(f"[-] Ошибка: Ядро Windows отказало в доступе к ОЗУ процесса {target_pid}.")
        print("    [!] Запустите утилиту от имени Администратора.\n")
        return None
        
    print(f"[+] Системный Handle успешно получен. Доступ к ОЗУ открыт.")
    
        
    
    class MEMORY_BASIC_INFORMATION(ctypes.Structure):
        _fields_ = [
            ("BaseAddress", ctypes.c_void_p),      
            ("AllocationBase", ctypes.c_void_p),
            ("AllocationProtect", ctypes.c_ulong),
            ("PartitionId", ctypes.c_ushort),
            ("RegionSize", ctypes.c_size_t),      
            ("State", ctypes.c_ulong),           
            ("Protect", ctypes.c_ulong),         
            ("Type", ctypes.c_ulong)
        ]

    mbi = MEMORY_BASIC_INFORMATION()
    current_address = 0

    max_address = 0x7FFFFFFFFFFF 

    kernel32.ReadProcessMemory.argtypes = [
        ctypes.c_void_p, 
        ctypes.c_void_p, 
        ctypes.c_void_p, 
        ctypes.c_size_t, 
        ctypes.c_void_p
    ]


    print("[*] Начинаю сканирование страниц памяти...\n")


    while current_address < max_address:
        
        if kernel32.VirtualQueryEx(process_handle, ctypes.c_void_p(current_address), ctypes.byref(mbi), ctypes.sizeof(mbi)) == 0:
            break

        
        if mbi.State == 0x1000 and mbi.Protect == 0x04:
            
            buffer = ctypes.create_string_buffer(mbi.RegionSize)
            bytes_read = ctypes.c_size_t(0)

           
            if kernel32.ReadProcessMemory(process_handle, mbi.BaseAddress, buffer, mbi.RegionSize, ctypes.byref(bytes_read)):
                
                raw_bytes = buffer.raw
                
                
                if bytes_read.value > 0:
                    raw_bytes = buffer.raw
                
                
                strings_found = re.findall(b"[ -~]{4,100}", raw_bytes)
                
                if strings_found:
                    for s in strings_found:
                        
                        decoded_str = s.decode('ascii', errors='ignore').strip()
                        
                        
                        if "http" in decoded_str.lower() or "www." in decoded_str.lower():
                            print(f"    [🚨 НАЙДЕНА СТРОКА В ОЗУ]: {decoded_str}")



        current_address += mbi.RegionSize


    kernel32.CloseHandle(process_handle)
    print("[+] Аудит памяти завершён.\n")

