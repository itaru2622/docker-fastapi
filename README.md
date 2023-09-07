## simple usage on linux:
```bash
docker run --rm -it -p 8000:8000 -v ${PWD}:/app itaru2622/fastapi:bookworm

# the above cmd start docker container  with:
pip3 install -r /app/requirements.txt
uvicorn main:app 
```

## other usage on linux:
you can:
- set any uvicorn options by opts environment.
- change requirement file path by py_requirements environment.
- change app name by app environment according to your implementation
```bash
docker run --rm -it -p 8000:8000 -v ${PWD}:${PWD} -w ${PWD} -e py_requirements=/app/requirements.txt  -e app=main:app -e opts='--host 0.0.0.0 --reload' itaru2622/fastapi:bookworm
# the above cmd start docker container  with:
pip3 install -r /app/requirements.txt
uvicorn --host 0.0.0.0 --reload main:app
```

## build docker image
```bash
docker build --build-arg base=python:3-bookworm --build-arg http_proxy=${http_proxy} --build-arg https_proxy=${https_proxy} -t itaru2622/fastapi:bookworm .
```
