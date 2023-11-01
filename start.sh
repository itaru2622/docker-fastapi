#!/bin/bash

if [ -r "${apt_requirements}" ]; then
   apt update; apt install -y `cat ${apt_requirements} | grep -v ^#`
fi

#
#  you can set upgrade-strategy for pip like: export pip_install_opt=--upgrade --upgrade-strategy eager
#
if [ -r "./setup.py" ] || [ -r "./setup.cfg" ] || [ -r "./pyproject.toml" ]; then
   pip3 install . ${pip_install_opt:=}
elif [ -r "${py_requirements}" ]; then
   echo "processsing ${py_requirements}"
   pip3 install -r  ${py_requirements} ${pip_install_opt:=}
fi

echo "starting fastapi with: uvicorn ${opts} ${app}"
/usr/bin/bash -c "uvicorn ${opts} ${app}"
