FROM maven:3.6.3-openjdk-11 AS maven_build

RUN apt-get update

COPY Dockerfiles/DebeziumCDC/app /tmp/

WORKDIR /tmp/

CMD ["mvn","spring-boot:run"]