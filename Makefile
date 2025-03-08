img  ?=itaru2622/fastapi:bookworm
base ?=python:3.12-bookworm

port ?=8000
sDir ?=/opt/fastapi-samples/3catchall
wDir ?=${PWD}

build:
	docker build --build-arg base=${base} --build-arg http_proxy=${http_proxy} --build-arg https_proxy=${https_proxy} --build-arg no_proxy=${no_proxy} -t ${img} .

# test embeded sample to check if fastapi works.
test:
	docker run -it --rm -p ${port}:8000 -w ${sDir} \
	-e http_proxy=${http_proxy} -e https_proxy=${https_proxy} -e no_proxy=${no_proxy} \
	-e app=main:app \
	-e opts='--host 0.0.0.0 --reload --reload-include "*.py" --reload-include "*.conf"' \
	-e pip_install_opt='--upgrade --upgrade-strategy eager' \
	${img}

# start your app, you can tune more as described in README.md, such as apt_requirements, and custom start.sh
start:
	docker run -it --rm -p ${port}:8000 -v ${wDir}:${wDir} -w ${wDir} \
	-e http_proxy=${http_proxy} -e https_proxy=${https_proxy} -e no_proxy=${no_proxy} \
	-e app=main:app \
	-e opts='--host 0.0.0.0 --reload --reload-include "*.py" --reload-include "*.conf"' \
	-e pip_install_opt='--upgrade --upgrade-strategy eager' \
	${img}
