@echo off
pushd %~dp0\..\..\
cd src/server
call celery -A server worker -l info -P gevent -c 8
popd