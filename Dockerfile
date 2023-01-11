FROM debian:bullseye

RUN apt update; \
    apt install -y python3-pip bash-completion git make jq vim ;

RUN pip3 install fastapi[standard] uvicorn requests bs4 Jinja2   q yq pytest pytest-cov httpx
RUN mkdir -p /app
COPY ./start.sh /usr/local/bin/start.sh
WORKDIR /app
ENV py_requirements=./requirements.txt
ENV app=main:app
ENV opts=''
CMD /usr/local/bin/start.sh
