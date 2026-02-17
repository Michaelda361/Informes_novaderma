@echo off
echo ========================================
echo   INSTALADOR COMPLETO DEL SISTEMA
echo ========================================
echo.
echo Este script instalara:
echo 1. Python 3.11.9
echo 2. Dependencias del proyecto (Flask, WeasyPrint, etc.)
echo 3. GTK3 Runtime (para generar PDFs)
echo.
echo Presiona cualquier tecla para continuar...
pause >nul

REM ============================================
REM PASO 1: VERIFICAR/INSTALAR PYTHON
REM ============================================
echo.
echo [1/3] Verificando Python...
echo.

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python no esta instalado. Instalando...
    echo.
    
    REM Descargar Python
    echo Descargando Python 3.11.9...
    if not exist "temp" mkdir temp
    powershell -Command "& {Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe' -OutFile 'temp\python-installer.exe'}"
    
    if not exist "temp\python-installer.exe" (
        echo ERROR: No se pudo descargar Python.
        echo Por favor descargalo manualmente desde: https://www.python.org/downloads/
        pause
        exit /b 1
    )
    
    echo Instalando Python...
    temp\python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1
    timeout /t 10 /nobreak >nul
    
    del temp\python-installer.exe
    rmdir temp
    
    echo Python instalado!
) else (
    echo Python ya esta instalado:
    python --version
)

REM ============================================
REM PASO 2: INSTALAR DEPENDENCIAS
REM ============================================
echo.
echo [2/3] Instalando dependencias del proyecto...
echo.

if not exist "requirements.txt" (
    echo ERROR: No se encuentra requirements.txt
    echo Asegurate de estar en la carpeta del proyecto.
    pause
    exit /b 1
)

echo Actualizando pip...
python -m pip install --upgrade pip

echo.
echo Instalando Flask, WeasyPrint, openpyxl, etc...
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo ERROR: Hubo un problema al instalar las dependencias.
    echo Intenta manualmente: pip install -r requirements.txt
    pause
    exit /b 1
)

echo.
echo Dependencias instaladas correctamente!

REM ============================================
REM PASO 3: INSTALAR GTK3 (OPCIONAL)
REM ============================================
echo.
echo [3/3] GTK3 Runtime (necesario para generar PDFs)
echo.
echo GTK3 debe instalarse manualmente.
echo.
echo ¿Deseas abrir la pagina de descarga de GTK3? (S/N)
set /p respuesta="> "

if /i "%respuesta%"=="S" (
    echo.
    echo Abriendo navegador...
    start https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
    echo.
    echo Descarga el archivo .exe mas reciente y ejecutalo.
    echo Luego presiona cualquier tecla para continuar...
    pause >nul
)

REM ============================================
REM VERIFICACION FINAL
REM ============================================
echo.
echo ========================================
echo   INSTALACION COMPLETADA
echo ========================================
echo.

echo Verificando instalacion...
echo.

python --version
echo.

python -c "import flask; print('Flask:', flask.__version__)"
python -c "import openpyxl; print('openpyxl:', openpyxl.__version__)"
python -c "import weasyprint; print('WeasyPrint:', weasyprint.__version__)"

echo.
echo ========================================
echo   TODO LISTO!
echo ========================================
echo.
echo Para iniciar la aplicacion:
echo 1. Cierra esta ventana
echo 2. Haz doble clic en: iniciar.bat
echo 3. O ejecuta: python app.py
echo.

pause
