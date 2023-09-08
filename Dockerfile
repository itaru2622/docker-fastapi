ARG base=debian:bullseye
FROM ${base}
ARG base

# use bash but not sh in RUN command
SHELL ["/bin/bash", "-c"]

RUN apt update;  apt install -y bash-completion git make jq vim less;
# install python3-pip and dependencies only when base image is not based on python
#   https://stackoverflow.com/questions/37057468/conditional-env-in-dockerfile
#   https://stackoverflow.com/questions/2172352/in-bash-how-can-i-check-if-a-string-begins-with-some-value
RUN if [[ ${base} != python* ]] ; \
    then \
        apt install -y python3-pip; \
    fi

RUN pip3 install install fastapi[standard] uvicorn[standard] requests bs4 Jinja2 q yq pytest pytest-cov httpx
RUN mkdir -p /app;    echo "set mouse-=a" > /root/.vimrc;
COPY ./start.sh /usr/local/bin/start.sh
WORKDIR /app
ENV py_requirements=./requirements.txt
ENV app=main:app
ENV opts=''
CMD /usr/local/bin/start.sh
