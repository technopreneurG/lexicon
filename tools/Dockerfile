FROM python:3

WORKDIR /lexicon-tools

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY docker-entrypoint /usr/bin

ENTRYPOINT [ "docker-entrypoint" ]

