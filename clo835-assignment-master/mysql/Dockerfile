FROM mysql:8.0
ENV MYSQL_DATABASE=appdb
ENV MYSQL_USER=app
ENV MYSQL_PASSWORD=apppass
ENV MYSQL_ROOT_PASSWORD=rootpass
COPY init.sql /docker-entrypoint-initdb.d/
