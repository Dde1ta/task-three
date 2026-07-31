FROM node:20-alpine AS builder

WORKDIR /app

COPY vite-project/*package*.json .

RUN npm i

COPY . .

ARG VITE_API_URL

ENV VITE_API_URL=$VITE_API_URL

RUN cd vite-project/ && npm run build

FROM nginx:alpine3.17

COPY --from=builder /app/vite-project/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
