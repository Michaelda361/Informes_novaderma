@echo off
echo ========================================
echo   INSTALADOR COMPLETO DEL SISTEMA
echo ========================================
echo.
echo Este script instalara:
echo 1. Python 3.11.9 (compatible con WeasyPrint)
echo 2. Dependencias del proyecto (Flask, WeasyPrint, etc.)
echo 3. GTK3 Runtime (para generar PDFs)
echo.
echo Presiona cualquier tecla para continuar...
pause >nul

REM ============================================
REM PASO 1: VERIFICAR/INSTALAR PYTHON
REM ============================================
echo.
echo [1/4] Verificando Python...
echo.

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python no esta instalado. Instalando Python 3.11.9...
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
    
    echo Instalando Python 3.11.9...
    temp\python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_pip=1
    timeout /t 15 /nobreak >nul
    
    del temp\python-installer.exe
    rmdir temp
    
    echo Python instalado! Reiniciando variables de entorno...
    refreshenv >nul 2>&1
    
    echo.
    echo IMPORTANTE: Cierra esta ventana y ejecuta el script de nuevo.
    pause
    exit /b 0
) else (
    echo Python ya esta instalado:
    python --version
)

REM ============================================
REM PASO 2: ACTUALIZAR PIP
REM ============================================
echo.
echo [2/4] Actualizando pip...
echo.

python -m pip install --upgrade pip

REM ============================================
REM PASO 3: INSTALAR DEPENDENCIAS
REM ============================================
echo.
echo [3/4] Instalando dependencias del proyecto...
echo.

if not exist "requirements.txt" (
    echo ERROR: No se encuentra requirements.txt
    echo Asegurate de estar en la carpeta del proyecto.
    pause
    exit /b 1
)

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
REM PASO 4: INSTALAR GTK3
REM ============================================
echo.
echo [4/4] GTK3 Runtime (NECESARIO para generar PDFs)
echo.
echo GTK3 debe instalarse manualmente para que WeasyPrint funcione.
echo Sin GTK3, NO se podran generar PDFs.
echo.
echo ¿Deseas abrir la pagina de descarga de GTK3? (S/N)
set /p respuesta="> "

if /i "%respuesta%"=="S" (
    echo.
    echo Abriendo navegador...
    start https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer/releases
    echo.
    echo INSTRUCCIONES:
    echo 1. Descarga el archivo .exe mas reciente
    echo 2. Ejecutalo con permisos de administrador
    echo 3. Acepta todas las opciones por defecto
    echo 4. Reinicia tu computadora despues de instalar
    echo.
    echo Presiona cualquier tecla cuando hayas instalado GTK3...
    pause >nul
)

REM ============================================
REM VERIFICACION FINAL
REM ============================================
echo.
echo ========================================
echo   VERIFICANDO INSTALACION
echo ========================================
echo.

python --version
echo.

python -c "import flask; print('✓ Flask:', flask.__version__)" 2>nul || echo "✗ Flask no instalado"
python -c "import openpyxl; print('✓ openpyxl:', openpyxl.__version__)" 2>nul || echo "✗ openpyxl no instalado"
python -c "import weasyprint; print('✓ WeasyPrint:', weasyprint.__version__)" 2>nul || echo "✗ WeasyPrint no instalado"
python -c "import PIL; print('✓ Pillow:', PIL.__version__)" 2>nul || echo "✗ Pillow no instalado"

echo.
echo ========================================
echo   INSTALACION COMPLETADA
echo ========================================
echo.
echo IMPORTANTE:
echo - Si instalaste GTK3, REINICIA tu computadora
echo - Despues del reinicio, ejecuta: iniciar.bat
echo.
echo Para iniciar la aplicacion:
echo 1. Haz doble clic en: iniciar.bat
echo 2. O ejecuta: python app.py
echo 3. Abre tu navegador en: http://localhost:5000
echo.

pause
