@echo off
title School MultiTool - By TVEGesd

:Menu
echo.
echo.
echo =====================================
echo    School Multitool - By TVEGesd
echo =====================================
echo 1. Math Calculator
echo 2. Schedule
echo 3. Studying
echo 4. English to Spanish Translator
echo 5. Exit
echo =====================================
echo.
set /p choice=Enter an option!: 

if "%choice%"==1" Goto Calculator
if "%choice%"==2" Goto Schedule
if "%choice%"==3" Goto Studying
if "%choice%"==4" Goto Translator
if "%choice%"==5" Goto exit

echo Invalid choice, Please try again
timeout /t 2 >nul
goto Menu

: Calculator
echo.
echo =====================================
echo           Math Calculator
echo =====================================
echo.
set /p experession=Enter an experession
set /a result=%experession%
echo Result=%experession%
echo.
timeout /t 2 >nul
goto Menu

: Schedule
echo.
echo =====================================
echo               Schedule
echo =====================================
echo.
echo 1. Put your first period here
echo 2. Put your second period here
echo 3. Put your third period here
echo 4. Put your fourth period here
echo 5. Put your fifth period here
echo 6. Put your sixth period here
echo 7. Put your seventh period here
echo 8. Put your eigth period here
echo 9. Put your ninth period here
echo =====================================
echo.

: Studying
echo. 
echo IDK what to put here you just write it yourself
echo.
timeout /t 2 >nul
goto Menu

: Translator
set /p english_word=Enter the word you want translated: 

if "%english_word" == "hello" (
    echo Hola
    echo to translate more select the option again
    echo I will add more translation words
    timeout /t 2 >nul
    goto menu
)

: Exit
echo Exiting program
echo ty for using this
timeout /t 2 >nul
exit
