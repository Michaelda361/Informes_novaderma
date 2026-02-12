@echo off
echo ========================================
echo  Generador de Reportes - Novaderma
echo ========================================
echo.

echo Verificando instalacion de Python...
python --version
if errorlevel 1 (
    echo ERROR: Python no esta instalado
    echo Descarga Python desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo.
echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo ========================================
echo  Iniciando servidor...
echo ========================================
echo.
echo Abre tu navegador en: http://localhost:5000
echo.
echo Presiona Ctrl+C para detener el servidor
echo.

python app.py

pause
