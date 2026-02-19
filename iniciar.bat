@echo off
echo ========================================
echo  Generador de Reportes - Novaderma
echo ========================================
echo.

REM Verificar Python
echo Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado
    echo.
    echo Ejecuta primero: instalar_todo.bat
    echo O descarga Python desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

python --version
echo.

REM Verificar dependencias
echo Verificando dependencias...
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo Instalando dependencias...
    python -m pip install -r requirements.txt
    if errorlevel 1 (
        echo.
        echo ERROR: No se pudieron instalar las dependencias
        echo Ejecuta: instalar_todo.bat
        pause
        exit /b 1
    )
) else (
    echo Dependencias OK
)

echo.
echo ========================================
echo  Iniciando servidor...
echo ========================================
echo.
echo La aplicacion se abrira en: http://localhost:5000
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

REM Abrir navegador automaticamente despues de 3 segundos
start /b timeout /t 3 /nobreak >nul && start http://localhost:5000

python app.py

pause
