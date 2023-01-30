#!/bin/bash

if [ -r "./setup.py" ] || [ -r "./setup.cfg" ] || [ -r "./pyproject.toml" ]; then
   pip3 install .
elif [ -r "${py_requirements}" ]; then
   echo "processsing ${py_requirements}"
   pip3 install -r  ${py_requirements}
fi

echo "starting fastapi with: uvicorn ${opts} ${app}"
uvicorn ${opts} ${app}
