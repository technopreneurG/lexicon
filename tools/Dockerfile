FROM python:3.7.1-stretch

#Few basic utitls needed for debugging
RUN apt-get update && apt-get install -y apt-utils unzip curl bash net-tools telnet

WORKDIR /lexicon-tools

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY docker-entrypoint /usr/bin

ENTRYPOINT [ "docker-entrypoint" ]

