@echo off
setlocal enabledelayedexpansion

:: Check if port number is provided
if "%1"=="" (
    echo Usage: killport ^<port^>
    echo Example: killport 8000
    exit /b 1
)

set PORT=%1

:: Validate port number (basic check)
echo %PORT%| findstr /r "^[0-9][0-9]*$" >nul
if errorlevel 1 (
    echo Error: Please provide a valid port number
    exit /b 1
)

:: Check for admin privileges
net session >nul 2>&1
if errorlevel 1 (
    echo Requesting administrator privileges...
    powershell -Command "Start-Process '%~f0' -ArgumentList '%*' -Verb RunAs"
    exit /b
)

echo Looking for processes on port %PORT%...

set FOUND=0

:: Find and kill processes using the specified port
for /f "tokens=5" %%a in ('netstat -ano ^| findstr ":%PORT%"') do (
    set PID=%%a
    if not "!PID!"=="" if not "!PID!"=="0" (
        set FOUND=1
        :: Get process name
        for /f "skip=1 tokens=1 delims=," %%b in ('tasklist /fi "pid eq !PID!" /fo csv /nh 2^>nul') do (
            set PROCESS_NAME=%%b
            set PROCESS_NAME=!PROCESS_NAME:"=!
            echo Found: !PROCESS_NAME! ^(PID: !PID!^)
        )
        
        echo Killing PID !PID!...
        
        :: Try multiple kill methods
        taskkill /f /pid !PID! >nul 2>&1
        if errorlevel 1 (
            echo Trying alternative method...
            wmic process where "ProcessId=!PID!" delete >nul 2>&1
            if errorlevel 1 (
                echo Warning: Could not kill PID !PID!
            ) else (
                echo Successfully killed PID !PID!
            )
        ) else (
            echo Successfully killed PID !PID!
        )
    )
)

if !FOUND!==0 (
    echo No processes found on port %PORT%
) else (
    echo.
    echo Verifying port %PORT% is now free...
    timeout /t 1 /nobreak >nul
    netstat -ano | findstr ":%PORT%" >nul
    if errorlevel 1 (
        echo Port %PORT% is now free!
    ) else (
        echo Warning: Some processes may still be using port %PORT%
        echo You may need to restart any services manually.
    )
)

echo.
echo Press any key to continue...
pause >nul

endlocal