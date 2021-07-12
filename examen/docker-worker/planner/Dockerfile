FROM node:14.0-buster

COPY  ./ app/

WORKDIR app/

ENV TASKS=4

RUN npm install -y

CMD node main.js

EXPOSE "3000"