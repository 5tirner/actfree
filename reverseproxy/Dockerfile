FROM nginx
COPY ./config/default.conf /etc/nginx/conf.d
RUN chmod -R 755 /usr/share/nginx/html
CMD [ "nginx", "-g", "daemon off;"]