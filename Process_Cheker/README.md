# GhostHound-Process-Scanner (v1.1.0 - Modular Update)

A modular, lightweight dynamic analysis utility designed for Malware Triage and live Windows Internals auditing. 

## 🦾 Key Features
* **Process Reconnaissance:** Scans active PIDs, names, and core system statuses.
* **Network Socket Auditor:** Tracks `ESTABLISHED` and `LISTEN` TCP/UDP sockets to detect hidden C2 connections.
* **Registry Autostart Monitor:** Extracts persistence mechanisms from `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`.
* **Path Resolution Module (New):** Resolves exact executable paths on the disk by PID or Process Name to detect masquerading.
* **x64 RAM String Extraction:** Performs direct virtual memory dumping of `PAGE_READWRITE` pages using Windows core WinAPI (`VirtualQueryEx`, `ReadProcessMemory`).
* **Active Response Module:** Features a 3-step threat eradication process (Process termination -> Registry cleanup -> File removal).

## 🛠️ Project Structure
* `main.py` - Core entry point with cyclic CLI menu.
* `process_core.py` - Process listing module.
* `network_general.py` - General socket tracker.
* `network_core.py` - Target process behavioral analyzer.
* `registry_core.py` - Registry persistence scanner.
* `memory_core.py` - Low-level RAM dumping engine (String Extraction).
* `response_core.py` - Active threat eradication engine.
* `path_check_name.py` - NEW: Executable path locator using Process Name.
* `path_check_pid.py` - NEW: Executable path locator using Target PID.

## ⚠️ Requirements
* Windows OS (x64 Architecture)
* Python 3.x / `psutil` library
* **Must be executed with Administrator privileges** to allow WinAPI kernel descriptors to open.
