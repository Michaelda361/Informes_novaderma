@echo off
echo ========================================
echo   SUBIR PROYECTO A GITHUB
echo ========================================
echo.

REM Verificar si Git está configurado
git config user.name >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git no esta configurado.
    echo Por favor ejecuta primero: configurar_git.bat
    echo.
    pause
    exit /b 1
)

echo Verificando estado de Git...
git status
echo.

REM Agregar todos los archivos
echo Agregando archivos...
git add .

REM Hacer commit
set /p mensaje="Ingresa el mensaje del commit (o presiona Enter para usar 'Actualizacion del proyecto'): "
if "%mensaje%"=="" set mensaje=Actualizacion del proyecto

echo.
echo Haciendo commit...
git commit -m "%mensaje%"

if errorlevel 1 (
    echo.
    echo ERROR al hacer commit.
    echo Verifica que Git este configurado correctamente.
    echo Ejecuta: configurar_git.bat
    echo.
    pause
    exit /b 1
)

echo.
echo ¿Ya creaste el repositorio en GitHub? (S/N)
set /p respuesta="> "

if /i "%respuesta%"=="S" (
    echo.
    echo Ingresa la URL de tu repositorio de GitHub:
    echo Ejemplo: https://github.com/tu-usuario/informes-novaderma.git
    set /p repo_url="> "
    
    echo.
    echo Configurando repositorio remoto...
    git remote remove origin 2>nul
    git remote add origin %repo_url%
    
    echo.
    echo Subiendo a GitHub...
    git branch -M main
    git push -u origin main
    
    if errorlevel 1 (
        echo.
        echo ERROR al subir a GitHub.
        echo Verifica que:
        echo 1. La URL del repositorio sea correcta
        echo 2. Tengas permisos para subir al repositorio
        echo 3. Hayas iniciado sesion en Git
        echo.
        pause
        exit /b 1
    )
    
    echo.
    echo ========================================
    echo   ¡EXITO! Proyecto subido a GitHub
    echo ========================================
    echo.
    echo Ahora puedes ir a Render.com para desplegarlo.
    echo.
) else (
    echo.
    echo ========================================
    echo   COMMIT REALIZADO EXITOSAMENTE
    echo ========================================
    echo.
    echo Pasos siguientes:
    echo 1. Ve a https://github.com/new
    echo 2. Crea un nuevo repositorio
    echo 3. Ejecuta este script de nuevo
    echo.
)

pause
