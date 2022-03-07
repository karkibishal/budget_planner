FROM python:3.8
WORKDIR /app
COPY . .
ENV DB_USER "$DB_USER"
ENV DB_PASSWORD "$DB_PASSWORD"
ENV DB_HOST "$DB_HOST"
ENV DB_PORT "$DB_PORT"
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["/usr/bin/python3", "app.py"]