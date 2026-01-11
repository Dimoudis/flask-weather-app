FROM python:3.12
WORKDIR /app-weather
COPY . /app-weather
#install libraries in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]