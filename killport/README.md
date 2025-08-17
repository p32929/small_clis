# KillPort

A Windows utility to kill processes running on a specific port. Useful for development when you need to free up ports occupied by stuck processes.

## Installation & Usage

### Prerequisites
- **Windows only** - uses built-in Windows commands (netstat, taskkill, wmic)

### Windows

The provided `killport.bat` script works on Windows.

1. **Run directly:**
   ```cmd
   killport.bat 8000
   ```

2. **Add to PATH (recommended):**
   
   **Option 1: Create a symbolic link (Windows 10+)**
   ```cmd
   # Run as Administrator
   mklink "C:\Windows\System32\killport.bat" "%CD%\killport.bat"
   ```
   
   **Option 2: Copy to PATH folder**
   ```cmd
   # Run as Administrator
   copy killport.bat "C:\Windows\System32\"
   ```

3. **Usage after installation:**
   ```cmd
   killport 8000
   ```

### Linux & macOS Alternatives

This utility is Windows-only, but here are equivalent one-liners for Unix systems:

```bash
# Using lsof (macOS/Linux)
sudo lsof -ti:8000 | xargs kill -9

# Using netstat (Linux)
sudo netstat -tlnp | grep :8000 | awk '{print $7}' | cut -d/ -f1 | xargs kill -9

# Using fuser (Linux)
sudo fuser -k 8000/tcp

# Using ss (modern Linux)
sudo ss -tlnp | grep :8000 | grep -oP 'pid=\K[0-9]+' | xargs kill -9
```

## Features

### Windows Version (`killport.bat`)
- ✅ **Admin privilege handling**: Automatically requests elevation when needed
- ✅ **Process identification**: Shows process name and PID before killing
- ✅ **Multiple kill methods**: Falls back to WMIC if taskkill fails
- ✅ **Port validation**: Ensures valid port number format
- ✅ **Verification**: Checks if port is actually freed after operation
- ✅ **Error handling**: Graceful handling of various error conditions


## Usage Examples

```cmd
# Kill process on port 8000
killport 8000

# Kill process on port 3000 (common React dev server)
killport 3000

# Kill process on port 5432 (PostgreSQL)
killport 5432

# Kill process on port 80 (HTTP)
killport 80
```

## Common Use Cases

- **Development servers**: Free up ports when dev servers don't shut down properly
- **Database connections**: Kill stuck database connections
- **Web servers**: Stop Apache/Nginx processes on specific ports
- **Node.js apps**: Kill Node processes that didn't terminate cleanly
- **Docker containers**: Free ports before starting new containers

## Troubleshooting

### Windows
- **"Access denied"**: Run Command Prompt as Administrator
- **"Process cannot be terminated"**: Some system processes cannot be killed
- **Script doesn't run**: Ensure batch file execution is allowed


## Security Notes

⚠️ **Important**: This tool forcefully terminates processes. Use with caution:
- Always verify which processes are using a port before killing
- Killing system processes may cause instability
- Some processes may need to be restarted manually
- Data loss may occur if processes are killed without proper shutdown

## Alternative Methods

### Windows PowerShell
```powershell
# Find and kill processes on port 8000
Get-NetTCPConnection -LocalPort 8000 | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
```

### macOS/Linux Terminal
```bash
# Using netstat and awk
netstat -tulpn | grep :8000 | awk '{print $7}' | cut -d/ -f1 | xargs kill -9

# Using fuser (if available)
fuser -k 8000/tcp
```

## License

This utility is provided as-is for development convenience. Use responsibly.