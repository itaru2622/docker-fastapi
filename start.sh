#!/bin/bash

if [ -r "${apt_requirements}" ]; then
   apt update; apt install -y `cat ${apt_requirements} | grep -v ^#`
fi

if [ -r "./setup.py" ] || [ -r "./setup.cfg" ] || [ -r "./pyproject.toml" ]; then
   pip3 install .
elif [ -r "${py_requirements}" ]; then
   echo "processsing ${py_requirements}"
#  you can set upgrade-strategy like: export py_requirements_opt=--upgrade --upgrade-strategy eager
   pip3 install -r  ${py_requirements} ${py_requirements_opt:=}
fi

echo "starting fastapi with: uvicorn ${opts} ${app}"
/usr/bin/bash -c "uvicorn ${opts} ${app}"
