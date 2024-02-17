FROM alpine

WORKDIR root

ARG name=Docker
ENV NAME=$name

COPY . .
ENTRYPOINT ["ash", "hello.sh"]

