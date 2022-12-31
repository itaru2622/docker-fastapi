#!/bin/bash

if [ -r "${py_requirements}" ]; then
   echo "processsing ${py_requirements}"
   pip3 install -r  ${py_requirements}
fi

echo "starting fastapi with: uvicorn ${opts} ${app}"
uvicorn ${opts} ${app}
