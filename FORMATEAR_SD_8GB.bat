@echo off
chcp 65001 > nul
:: Eleva permisos a Administrador automáticamente si es necesario
net session >nul 2>&1
if %errorlevel% neq 0 (
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)

title Formateador de Tarjeta SD 8GB (Disco 2)
echo ============================================================
echo      FORMATEANDO TARJETA SD 8GB (DISCO 2) A FAT32
echo ============================================================
echo.

(
echo select disk 2
echo clean
echo rescan
echo select disk 2
echo convert mbr
echo create partition primary
echo format fs=fat32 quick label="SD_8GB"
echo assign
echo exit
) > "%TEMP%\diskpart_sd.txt"

diskpart /s "%TEMP%\diskpart_sd.txt"
del "%TEMP%\diskpart_sd.txt"

echo.
echo ============================================================
echo    ¡PROCESO COMPLETADO! COMPRUEBA SI APARECE LA UNIDAD SD_8GB.
echo ============================================================
echo.
pause
