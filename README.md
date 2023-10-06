## simple usage on linux:
```bash
docker run --rm -it -p 8000:8000 -v ${PWD}:/app itaru2622/fastapi:bookworm

# the above cmd start docker container  with:
apt  install -y /app/requirements-apt.txt
pip3 install -r /app/requirements.txt
uvicorn main:app 
```

## other usage on linux:
you can:
- set any uvicorn options by opts environment variable.
- change requirement file path for apt install by apt_requirements environment variable.
- change requirement file path for pip install by py_requirements  environment variable.
- change app name by app environment according to your implementation
```bash
docker run --rm -it -p 8000:8000 -v ${PWD}:${PWD} -w ${PWD} -e py_requirements=${PWD}/requirements.txt -e apt_requirements=${PWD}/requirements-apt.txt -e app=main:app -e opts='--host 0.0.0.0 --reload --reload-include "*.py" --reload-include "*.conf"' itaru2622/fastapi:bookworm
# the above cmd start docker container  with:
apt  install -y ${apt_requirements}
pip3 install -r ${py_requirements}
uvicorn ${opts} ${app}
```

## build docker image
```bash
docker build --build-arg base=python:3-bookworm --build-arg http_proxy=${http_proxy} --build-arg https_proxy=${https_proxy} -t itaru2622/fastapi:bookworm .
```
