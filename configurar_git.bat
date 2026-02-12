@echo off
echo ========================================
echo   CONFIGURACION DE GIT
echo ========================================
echo.

set /p nombre="Ingresa tu nombre: "
set /p email="Ingresa tu email: "

echo.
echo Configurando Git...
git config --global user.name "%nombre%"
git config --global user.email "%email%"

echo.
echo ¡Configuracion completada!
echo.
echo Nombre: %nombre%
echo Email: %email%
echo.

pause
