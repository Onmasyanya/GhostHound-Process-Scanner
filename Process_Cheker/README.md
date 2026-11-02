# GhostHound-Process-Scanner (v1.1.0)

An experimental Windows process inspection and system monitoring utility written in Python.

GhostHound is an educational project focused on exploring Windows process management, network connections, registry startup entries, executable paths, and basic process memory inspection.

## 🦾 Features

### 1. Process Enumeration
- Lists currently running Windows processes.
- Retrieves process IDs (PIDs), names, and statuses.
- Saves process information to a text report.

### 2. Network Connection Inspection
- Retrieves TCP and UDP connection information using `psutil`.
- Displays local and remote addresses, ports, and connection states.
- Supports inspection of network connections across all processes or a selected process.
- Saves network inspection results to text reports.

### 3. Registry Autostart Inspection
- Reads startup entries from:
  `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`
- Displays registry value names and associated startup paths.

### 4. Executable Path Resolution
- Resolves executable paths using a process PID.
- Searches for a running process by name and retrieves its executable path.
- Provides basic information that can help investigate unusual executable locations.

### 5. Process Memory String Extraction
- Uses Windows API functions:
  - `OpenProcess`
  - `VirtualQueryEx`
  - `ReadProcessMemory`
  - `CloseHandle`
- Inspects accessible memory regions marked as `PAGE_READWRITE`.
- Searches for printable ASCII strings between 4 and 100 characters.
- Displays extracted strings containing `http` or `www.`.

### 6. Experimental Response Module
- Terminates a selected process.
- Optionally removes a specified value from the user's Run registry key.
- Optionally deletes a user-specified file.

These operations are experimental and require careful manual selection of their targets.

## 🛠️ Project Structure

All source files are located in the `Process_Cheker/` directory.

- `main.py` — Main entry point and interactive command-line menu.
- `process_core.py` — Process enumeration and text report generation.
- `network_general.py` — Network connection inspection across running processes.
- `network_core.py` — Network connection inspection for a selected process.
- `registry_core.py` — Windows registry startup entry inspection.
- `memory_core.py` — Process memory inspection and ASCII string extraction.
- `response_core.py` — Experimental process termination, registry value removal, and file deletion.
- `path_check_name.py` — Executable path lookup by process name.
- `path_check_pid.py` — Executable path lookup by process PID.

## ⚙️ Requirements

- Windows operating system.
- 64-bit Windows environment for the implemented memory address range.
- Python 3.x.
- `psutil` Python package.

Install the dependency:

```bash
pip install psutil
```

Administrator privileges may be required for inspecting certain processes and accessing protected process memory.

## ⚠️ Limitations

GhostHound is an experimental educational utility, not a full antivirus or a validated malware detection product.

- Network connection information does not independently identify malicious C2 activity.
- Registry startup entries are inspected only in the specified `HKCU` Run location.
- Memory inspection is limited to accessible `PAGE_READWRITE` regions and the implemented ASCII string extraction logic.
- Extracted URLs and strings are informational indicators, not proof of malicious activity.
- Executable path inspection does not independently determine whether a file is malicious.
- Response operations do not guarantee complete malware removal and may affect legitimate processes or files if incorrect targets are selected.

Use the response module with caution.

## 📌 Project Status

**Version:** 1.1.0 — Modular Update

GhostHound is an early educational project documenting my first experiments with Python, Windows internals, process inspection, and system-level APIs.

Development focus has since moved to **VANTHEX**, a C++-based Windows system inspection project.
