# Get Files

A simple Python utility that collects all file contents in a directory and saves them to a single output file.

## Installation & Usage

### Prerequisites
- Python 3.x installed on your system

### Linux & macOS

1. **Make the script executable:**
   ```bash
   chmod +x get-files.py
   ```

2. **Install globally (optional):**
   ```bash
   # Option 1: Create a symbolic link (recommended)
   sudo ln -s $(pwd)/get-files.py /usr/local/bin/get-files
   
   # Option 2: Copy to a directory in your PATH
   sudo cp get-files.py /usr/local/bin/get-files
   ```

3. **Run the tool:**
   ```bash
   # If installed globally
   get-files
   
   # Or run directly
   ./get-files.py
   ```

### Windows

1. **Run directly with Python:**
   ```cmd
   python get-files.py
   ```

2. **Add to PATH (optional):**
   
   **Option 1: Create a symbolic link (Windows 10+)**
   ```cmd
   # Run as Administrator
   mklink "C:\Windows\System32\get-files.py" "%CD%\get-files.py"
   ```
   
   **Option 2: Create a batch file**
   - Create `get-files.bat` in a folder that's in your PATH:
     ```batch
     @echo off
     python "C:\path\to\your\get-files.py" %*
     ```
   
   **Option 3: Copy to PATH folder**
   ```cmd
   copy get-files.py "C:\Windows\System32\"
   ```

3. **Alternative - PowerShell:**
   ```powershell
   python .\get-files.py
   ```

## How it works

1. Run the script in any directory
2. Choose whether to include subdirectories (y/n)
3. The tool will create an `output.txt` file containing all file contents
4. Each file's content is wrapped in markdown code blocks with the filename as a comment

## Output Format

The generated `output.txt` file will contain:
```
// filename1.txt
```
[file content here]
```

// filename2.py
```
[file content here]
```
```