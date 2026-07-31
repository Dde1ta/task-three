FROM node:alpine3.11 AS builder

WORKDIR /app

COPY vite-project/*package*.json .

RUN npm i

COPY vite-project/* .

RUN npm build

FROM nginx:alpine3.17

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
