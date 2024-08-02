@echo off
pushd %~dp0\..\..\
call python src\server\manage.py runserver
popd