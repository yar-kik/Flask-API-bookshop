FROM node

EXPOSE 3000
EXPOSE 35729

WORKDIR /client

COPY package.json /client/package.json
COPY package-lock.json /client/package-lock.json

RUN npm install
RUN npm install react-scripts -g

COPY . /client

CMD ["npm", "start"]