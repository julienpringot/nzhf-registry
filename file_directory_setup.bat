@echo off

REM Create project root directory
mkdir project-root
cd project-root

REM Create web-ui directory
mkdir web-ui
cd web-ui
mkdir src public
echo {} > package.json
cd ..

REM Create web-service directory
mkdir web-service
cd web-service
mkdir app config tests
echo. > requirements.txt
cd ..

REM Create database directory
mkdir database
cd database
mkdir migrations scripts
cd ..

REM Create docs directory
mkdir docs

REM Create project root files
echo. > .gitignore
echo. > README.md
echo. > LICENSE
