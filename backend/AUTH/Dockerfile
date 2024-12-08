FROM python:3
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
RUN pip install --upgrade pip
RUN pip install django
RUN pip install django_rest_framework
RUN pip install djangorestframework_simplejwt[crypto]
RUN pip install requests
RUN pip install python-dotenv
RUN pip install Pillow
WORKDIR /work
COPY ./auth .
COPY ./start .
RUN chmod +x start.sh
CMD [ "./start.sh" ]
