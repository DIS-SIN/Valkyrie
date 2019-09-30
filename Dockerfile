FROM tiangolo/meinheld-gunicorn-flask:python3.7
ENV APP_MODULE app:application
ENV PORT 5000
ENV GOOGLE_APPLICATION_CREDENTIALS ./credentials/google.json
RUN pip install --upgrade pip
COPY . /app
RUN pip install -r requirements.txt