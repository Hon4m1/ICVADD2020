FROM node:14.0-buster

COPY  ./ app/

WORKDIR app/

ENV MULT=True

ENV ADD=True

RUN npm install -y

CMD node main.js

EXPOSE "3000"