@echo off
echo ========================================
echo  EMPAQUETAR PARA OTRO EQUIPO
echo ========================================
echo.

set CARPETA_DESTINO=novaderma_portable

echo Creando carpeta de distribucion...
if exist %CARPETA_DESTINO% rmdir /s /q %CARPETA_DESTINO%
mkdir %CARPETA_DESTINO%

echo.
echo Copiando archivos necesarios...

REM Archivos principales
copy app.py %CARPETA_DESTINO%\
copy requirements.txt %CARPETA_DESTINO%\
copy iniciar.bat %CARPETA_DESTINO%\
copy README.md %CARPETA_DESTINO%\
copy INSTALACION_NUEVO_EQUIPO.txt %CARPETA_DESTINO%\
copy GUIA_RAPIDA.md %CARPETA_DESTINO%\

REM Carpetas
xcopy /E /I templates %CARPETA_DESTINO%\templates
xcopy /E /I static %CARPETA_DESTINO%\static

REM Crear carpetas vacias
mkdir %CARPETA_DESTINO%\uploads
mkdir %CARPETA_DESTINO%\output

echo.
echo ========================================
echo  EMPAQUETADO COMPLETADO
echo ========================================
echo.
echo Carpeta creada: %CARPETA_DESTINO%
echo.
echo Ahora puedes:
echo 1. Comprimir la carpeta "%CARPETA_DESTINO%" en un ZIP
echo 2. Copiar el ZIP al otro equipo
echo 3. Descomprimir y seguir INSTALACION_NUEVO_EQUIPO.txt
echo.
pause
