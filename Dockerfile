FROM python

RUN apt-get update && apt-get install -y postgresql-client
COPY ./requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

ENV POSTGRES_DB='amazon'
ENV POSTGRES_USER='workshop_user'

ENV POSTGRES_PASSWORD='workshop_user1'

ENV POSTGRES_HOST='172.20.3.48'
ENV POSTGRES_PORT='5435'

ENV ES_HOST='172.20.3.48'
ENV ES_PORT='9200'

COPY ./ ./

WORKDIR src/app/
