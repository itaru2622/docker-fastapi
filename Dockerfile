FROM debian:bullseye

RUN apt update; \
    apt install -y python3-pip bash-completion git make jq ;

RUN pip3 install fastapi uvicorn yq q pytest pytest-cov
RUN mkdir -p /app
COPY ./start.sh /usr/local/bin/start.sh
WORKDIR /app
ENV py_requirements=/app/requirements.txt
ENV app=main:app
ENV opts=''
CMD /usr/local/bin/start.sh
