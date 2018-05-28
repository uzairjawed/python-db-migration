FROM ubuntu:16.04
RUN apt-get update 
RUN apt-get install -y mysql-client python2.7 python-pip vim python2.7-mysqldb

ADD ./create-db-schema.sh /usr/local/bin/create-db-schema.sh
RUN chmod 777 /usr/local/bin/create-db-schema.sh

CMD ["/usr/local/bin/create-db-schema.sh mysql ecs ecs ecs"]

ENTRYPOINT /bin/bash 